import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

type ViteConfigInput = {
  mode: string;
  command: string;
}

export default (args: ViteConfigInput) => {
  const generateScopedName = args.mode === 'development' ? '[local]_[hash:base64:2]' : '[hash:base64:8]'

  return defineConfig({
    resolve: {
      alias: {
        '@': path.resolve(__dirname, './src'),
        '@ui': path.resolve(__dirname, './src/ui'),
        '@static': path.resolve(__dirname, './static'),
        '@components': path.resolve(__dirname, './src/components'),
      },
    },
    plugins: [react()],
    css: {
      modules: {
        localsConvention: 'camelCase',
        generateScopedName
      }
    }
  })
}
