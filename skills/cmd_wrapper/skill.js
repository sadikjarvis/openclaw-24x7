const { exec } = require('child_process');

module.exports = async function (input, context) {
  const raw = context.message || '';
  const cmd = raw.replace(/^Run command:\s*/i, '').trim();
  if (!cmd) return '❌ No command supplied.';

  return new Promise((resolve) => {
    exec(cmd, (err, stdout, stderr) => {
      if (err) {
        const msg = stdout + stderr || err.message;
        resolve(`❌ ${msg}`);
      } else {
        resolve(stdout + stderr);
      }
    });
  }).then(out => out.trim());
};
