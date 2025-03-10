import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'node:path';
import process from 'node:process';

const root = process.cwd();
const pathResolve = (pathname: string) => resolve(root, '.', pathname);
// https://vite.dev/config/
export default defineConfig({
  resolve: {
    alias: [
      {
        find: "@",
        replacement: pathResolve(`src`)
      }
    ]
  },
  plugins: [vue()],
})
