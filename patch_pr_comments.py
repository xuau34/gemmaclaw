import re

with open("src/commands/benchmark-gemma.ts", "r") as f:
    content = f.read()

# Add import to the top
if 'import { addDockerGpuArgs, detectHardware } from "../gemmaclaw/provision/hardware.js";' not in content:
    content = content.replace(
        'import path from "node:path";\n',
        'import path from "node:path";\nimport { addDockerGpuArgs, detectHardware } from "../gemmaclaw/provision/hardware.js";\n'
    )

# Remove dynamic imports inside the function
content = re.sub(r'  const \{ detectHardware \} = await import\("\.\./gemmaclaw/provision/hardware\.js"\);\n', '', content)

with open("src/commands/benchmark-gemma.ts", "w") as f:
    f.write(content)
