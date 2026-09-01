from client import LightweightLocalModelDaemonLifecycleManagerClient

def main():
    client = LightweightLocalModelDaemonLifecycleManagerClient()
    res = client.manage_daemon_model_lifecycle('deepseek-r1:1.5b-q8_0', 'WARM_LOAD')
    print('Local Model Daemon: ' + res['daemon_task_id'] + ' (' + res['model_tag'] + ')')
    print('Action: ' + res['action_executed'] + ' | VRAM: ' + str(res['gpu_vram_allocated_gb']) + ' GB')
    print('Swap Latency: ' + str(res['cold_start_swap_latency_ms']) + 'ms')
    print('Endpoint: ' + res['local_http_inference_endpoint'])

if __name__ == '__main__':
    main()
