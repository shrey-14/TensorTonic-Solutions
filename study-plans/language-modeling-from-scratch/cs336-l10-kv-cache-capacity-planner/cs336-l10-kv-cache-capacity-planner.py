import math

def kv_cache_capacity_planner(
    model_parameters: int, bytes_per_parameter: int, num_layers: int,
    sequence_length: int, num_attention_heads: int, num_kv_heads: int,
    head_dim: int, bytes_per_element: int, memory_per_gpu: int,
    reserved_memory: int, memory_bandwidth: int,
) -> dict:
    """
    Returns a dict: model_bytes, kv_bytes_per_request, max_batch_size, seconds_per_token, tokens_per_second.
    """
    d = {"model_bytes":0,"kv_bytes_per_request":0,"max_batch_size":0,"seconds_per_token":0,"tokens_per_second":0}
    
    d['model_bytes'] = model_parameters * bytes_per_parameter
    
    d['kv_bytes_per_request'] = 2 * num_layers * sequence_length * num_kv_heads * head_dim * bytes_per_element

    d['max_batch_size'] = round(max(0, math.floor((memory_per_gpu - reserved_memory - d['model_bytes']) / (d['kv_bytes_per_request']))))

    d['seconds_per_token'] = (d['model_bytes'] + d['max_batch_size'] * d['kv_bytes_per_request']) / memory_bandwidth

    d['tokens_per_second'] = d['max_batch_size'] / d['seconds_per_token']

    return d

    

    
    
