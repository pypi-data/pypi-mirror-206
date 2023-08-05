from functools import partial
from typing import Dict, Union, Callable, Type

import torch
from torch import nn
from torch.nn.modules import loss

from eir.data_load import data_utils
from eir.setup import schemas
from eir.setup.output_setup import al_output_objects_as_dict
from eir.train_utils.metrics import calculate_prediction_losses

al_criteria = Dict[str, Dict[str, Union[nn.CrossEntropyLoss, nn.MSELoss]]]
al_losses_classes = [Type[i] for i in loss.__all__]


def _get_criteria(outputs_as_dict: al_output_objects_as_dict) -> al_criteria:
    criteria_dict = {}
    target_columns_gen = data_utils.get_output_info_generator(
        outputs_as_dict=outputs_as_dict
    )

    for output_name, column_type, column_name in target_columns_gen:
        label_smoothing = _get_label_smoothing(
            output_config=outputs_as_dict[output_name].output_config,
            column_type=column_type,
        )

        criterion = get_criterion(
            column_type_=column_type, cat_label_smoothing_=label_smoothing
        )

        if output_name not in criteria_dict:
            criteria_dict[output_name] = {}
        criteria_dict[output_name][column_name] = criterion

    return criteria_dict


def build_loss_dict() -> Dict[str, Type[nn.Module]]:
    all_losses = loss.__all__

    loss_dict = {}

    return loss_dict


def get_criterion(
    column_type_: str, cat_label_smoothing_: float = 0.0
) -> Union[nn.CrossEntropyLoss, Callable]:
    if column_type_ == "con":
        assert cat_label_smoothing_ == 0.0
        return partial(_calc_mse, mse_loss_func=nn.MSELoss())
    elif column_type_ == "cat":
        return nn.CrossEntropyLoss(label_smoothing=cat_label_smoothing_)


def _get_label_smoothing(
    output_config: schemas.OutputConfig,
    column_type: str,
) -> float:
    if column_type == "con":
        return 0.0
    elif column_type == "cat":
        return output_config.output_type_info.cat_label_smoothing

    raise ValueError(f"Unknown column type: {column_type}")


def _calc_mse(input: torch.Tensor, target: torch.Tensor, mse_loss_func: nn.MSELoss):
    return mse_loss_func(input=input.squeeze(), target=target.squeeze())


def _get_loss_callable(criteria: al_criteria):
    single_task_loss_func = partial(calculate_prediction_losses, criteria=criteria)
    return single_task_loss_func
