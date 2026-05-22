import re

with open("src/commands/benchmark-gemma.ts", "r") as f:
    content = f.read()

content = re.sub(
    r'  const hw = detectHardware\(\);\n  if \(hw\.gpu\.nvidia \|\| opts\.gpuLayers \!= null\) \{\n    args\.push\("--gpus", "all"\);\n  \}',
    r'  addDockerGpuArgs(args, detectHardware(), { gpuLayers: opts.gpuLayers });',
    content
)

content = re.sub(
    r'  const hw = detectHardware\(\);\n  if \(hw\.gpu\.nvidia\) \{\n    createArgs\.push\("--gpus", "all"\);\n  \}',
    r'  addDockerGpuArgs(createArgs, detectHardware());',
    content
)

with open("src/commands/benchmark-gemma.ts", "w") as f:
    f.write(content)
