const { spawn } = require('child_process');

module.exports = async function (input, context) {
  const raw = context.message || '';
  const svc = raw.replace(/^Run command:\s*/i, '').trim();
  if (!svc) return '❌ No command supplied.';

  try {
    const ps = spawn('powershell', ['-NoLogo', '-NonInteractive', '-Command', svc], { stdio: 'pipe' });

    let out = '';
    ps.stdout.on('data', chunk => out += chunk.toString());
    ps.stderr.on('data', chunk => out += chunk.toString());

    await new Promise((resolve, reject) => {
      ps.on('close', (code) => {
        if (code !== 0) reject(`Exit code ${code}`);
        else resolve();
      });
      ps.on('error', reject);
    });

    return out.trim();
  } catch (e) { return `❌ ${e}`; }
};
