"""
Copyright (c) Microsoft Corporation
Licensed under the MIT license.
"""

#########################################
# ZeRO optimization
#########################################
# ZeRO optimization. By default, this optimization is not enabled.
# Users have to configure the desired optimization (0 means disabled) in params.json as below example:
ZERO_FORMAT = '''
ZeRO optimization should be enabled as:
"session_params": {
  "zero_optimization": {
    "stage": [0|1|2],
    "allgather_partitions": [true|false],
    "allgather_bucket_size": 500000000,
    "reduce_scatter": [true|false],
    "contiguous_gradients" : [true|false]
    "overlap_comm": [true|false],
    "reduce_bucket_size": 500000000
    "load_from_fp32_weights": [true|false]
    "cpu_offload": [true|false]
    }
}
'''

ZERO_OPTIMIZATION = 'zero_optimization'
ZERO_OPTIMIZATION_DISABLED = 0
ZERO_OPTIMIZATION_OPTIMIZER_STATES = 1
ZERO_OPTIMIZATION_GRADIENTS = 2
ZERO_OPTIMIZATION_WEIGHTS = 3
MAX_STAGE_ZERO_OPTIMIZATION = ZERO_OPTIMIZATION_GRADIENTS

ZERO_OPTIMIZATION_STAGE = 'stage'
ZERO_OPTIMIZATION_STAGE_1 = 'stage_1'
ZERO_OPTIMIZATION_STAGE_2 = 'stage_2'
ZERO_OPTIMIZATION_STAGE_3 = 'stage_3'

ZERO_OPTIMIZATION_STAGE_DEFAULT = ZERO_OPTIMIZATION_DISABLED

ZERO_OPTIMIZATION_ALLGATHER_PARTITIONS = 'allgather_partitions'
ZERO_OPTIMIZATION_ALLGATHER_PARTITIONS_DEFAULT = True

ZERO_OPTIMIZATION_REDUCE_SCATTER = 'reduce_scatter'
ZERO_OPTIMIZATION_REDUCE_SCATTER_DEFAULT = True

ZERO_OPTIMIZATION_OVERLAP_COMM = 'overlap_comm'
ZERO_OPTIMIZATION_OVERLAP_COMM_DEFAULT = False

ZERO_OPTIMIZATION_CONTIGUOUS_GRADIENTS = 'contiguous_gradients'
ZERO_OPTIMIZATION_CONTIGUOUS_GRADIENTS_DEFAULT = False

ZERO_OPTIMIZATION_REDUCE_BUCKET_SIZE = 'reduce_bucket_size'
ZERO_OPTIMIZATION_REDUCE_BUCKET_SIZE_DEFAULT = 500000000

ZERO_OPTIMIZATION_ALLGATHER_BUCKET_SIZE = 'allgather_bucket_size'
ZERO_OPTIMIZATION_ALLGATHER_BUCKET_SIZE_DEFAULT = 500000000
ZERO_OPTIMIZATION_ALLGATHER_BUCKET_SIZE_DEPRECATED = 'allgather_size'
ZERO_OPTIMIZATION_LOAD_FROM_FP32_WEIGHTS = 'load_from_fp32_weights'
ZERO_OPTIMIZATION_LOAD_FROM_FP32_WEIGHTS_DEFAULT = True

ZERO_OPTIMIZATION_CPU_OFFLOAD = 'cpu_offload'
ZERO_OPTIMIZATION_CPU_OFFLOAD_DEFAULT = False

ZERO_OPTIMIZATION_ELASTIC_CHECKPOINT = 'elastic_checkpoint'
ZERO_OPTIMIZATION_ELASTIC_CHECKPOINT_DEFAULT = True

ZERO_OPTIMIZATION_DEFAULT = {
    ZERO_OPTIMIZATION_STAGE: ZERO_OPTIMIZATION_STAGE_DEFAULT,
    ZERO_OPTIMIZATION_CONTIGUOUS_GRADIENTS:
    ZERO_OPTIMIZATION_CONTIGUOUS_GRADIENTS_DEFAULT,
    ZERO_OPTIMIZATION_REDUCE_SCATTER: ZERO_OPTIMIZATION_REDUCE_SCATTER_DEFAULT,
    ZERO_OPTIMIZATION_REDUCE_BUCKET_SIZE: ZERO_OPTIMIZATION_REDUCE_BUCKET_SIZE_DEFAULT,
    ZERO_OPTIMIZATION_ALLGATHER_PARTITIONS:
    ZERO_OPTIMIZATION_ALLGATHER_PARTITIONS_DEFAULT,
    ZERO_OPTIMIZATION_ALLGATHER_BUCKET_SIZE:
    ZERO_OPTIMIZATION_ALLGATHER_BUCKET_SIZE_DEFAULT,
    ZERO_OPTIMIZATION_LOAD_FROM_FP32_WEIGHTS:
    ZERO_OPTIMIZATION_LOAD_FROM_FP32_WEIGHTS_DEFAULT,
    ZERO_OPTIMIZATION_CPU_OFFLOAD: ZERO_OPTIMIZATION_CPU_OFFLOAD_DEFAULT,
    ZERO_OPTIMIZATION_ELASTIC_CHECKPOINT:
    ZERO_OPTIMIZATION_ELASTIC_CHECKPOINT_DEFAULT
}
