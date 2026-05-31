import { execSync } from 'child_process';
try {
  execSync('node dist/gemmaclaw/benchmark/cli-standalone.js agent --ollama-url http://127.0.0.1:11434 --mock', { stdio: 'inherit' });
} catch (e) {
  console.error(e);
}
