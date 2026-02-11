
const g = require('fs');
const path = require('path');

function registerSkill(skillPath) {
  const skillName = path.basename(skillPath);
  const isExists = fs.existsSync(path.join(skillPath, 'skill.js'));
  if (!isExists) throw new Error('skill.js missing');
  // Write a small registration file
  const regPath = path.join(skillPath, '__register__.js');
  const content = `
require(path.join(__dirname, 'skill.js'));
`;
  fs.writeFileSync(regPath, content);
}
registerSkill('C:\\Users\\Md Sadik Laskar\\.openclaw\\skills\\cmd_executor');
