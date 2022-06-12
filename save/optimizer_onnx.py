import onnx
import onnxoptimizer

onnxfile = 'C:\\MyData\\Code\\project\\FaceRecognition\\projectAI_FCode\\model\\ultra_light_640_2.onnx'
onnx_model = onnx.load(onnxfile)
passes = ["base_net.7.branch1.0.bn.num_batches_tracked", "base_net.11.4.num_batches_tracked"]
# , "base_net.0.1.num_batches_tracked", "base_net.8.4.num_batches_tracked", "base_net.1.1.num_batches_tracked", "base_net.10.1.num_batches_tracked", "base_net.1.4.num_batches_tracked", "base_net.11.1.num_batches_tracked", "base_net.10.4.num_batches_tracked", "base_net.12.1.num_batches_tracked", "base_net.12.4.num_batches_tracked", "base_net.2.4.num_batches_tracked", "base_net.2.1.num_batches_tracked", "base_net.3.1.num_batches_tracked", "base_net.3.4.num_batches_tracked", "base_net.4.1.num_batches_tracked", "base_net.8.1.num_batches_tracked", "base_net.4.4.num_batches_tracked"]
optimized_model = onnxoptimizer.optimize(onnx_model, passes)
print('success')

onnx.save(optimized_model, onnxfile)