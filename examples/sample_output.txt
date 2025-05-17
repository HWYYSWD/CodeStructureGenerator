const fs = require('fs');
const path = require('path');

const TEMPLATES = {
  basic_webapp: [
    'src/',
    'public/css/',
    'public/js/',
    'tests/',
    'docs/',
    '.gitignore',
    'README.md'
  ]
};

function generateStructure(outputDir, template = 'basic_webapp') {
  TEMPLATES[template].forEach(item => {
    const fullPath = path.join(outputDir, item);
    
    if (item.endsWith('/')) {
      fs.mkdirSync(fullPath, { recursive: true });
      console.log(`📁 Created directory: ${fullPath}`);
    } else {
      fs.writeFileSync(fullPath, '// Auto-generated file');
      console.log(`📄 Created file: ${fullPath}`);
    }
  });
}

// 命令行参数处理
const args = process.argv.slice(2);
const outputDir = args[0] || 'new_project';
const template = args.find(arg => arg.startsWith('-t'))?.split('=')[1] || 'basic_webapp';

generateStructure(outputDir, template);
