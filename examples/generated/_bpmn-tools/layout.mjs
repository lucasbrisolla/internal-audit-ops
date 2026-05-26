import { readFileSync, writeFileSync } from 'fs';
import { layoutProcess } from 'bpmn-auto-layout';

const input = readFileSync(process.argv[2], 'utf8');
const output = await layoutProcess(input);
writeFileSync(process.argv[3], output);
console.log('Layout done →', process.argv[3]);
