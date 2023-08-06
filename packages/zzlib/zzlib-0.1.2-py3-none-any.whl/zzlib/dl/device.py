import socket


def check_cuda(platforms=[]):
    """
    Prints the hostname, tensorflow version, pytorch version, jax version,
    and number of GPUs available.
    :param platforms: A list of platforms to check.
    """
    print(f"Host: {socket.gethostname()}")
    if not platforms or "pytorch" in platforms:
        try:
            import torch
        except ImportError:
            pass
        else:
            print(f"PyTorch: {torch.__version__}")
            print(f" - Built with CUDA: {torch.version.cuda}")
            print(f" - CUDA available: {torch.cuda.is_available()}")
            print(f" - Num GPUs available: {torch.cuda.device_count()}")
            for i in range(torch.cuda.device_count()):
                print(f"  - GPU {i}: {torch.cuda.get_device_name(i)}")
    if not platforms or "tensorflow" in platforms:
        try:
            import tensorflow as tf
        except ImportError:
            pass
        else:
            print(f"Tensorflow: {tf.__version__}")
            print(f" - Built with CUDA: {tf.test.is_built_with_cuda()}")
            print(f' - Num GPUs available: {len(tf.config.list_physical_devices("GPU"))}')
    if not platforms or "jax" in platforms:
        try:
            import jax
        except ImportError:
            pass
        else:
            jax_gpus = [d for d in jax.devices() if d.platform != "cpu"]
            print(f"Jax: {jax.__version__}")
            print(f" - Num GPUs available: {len(jax_gpus)}")
