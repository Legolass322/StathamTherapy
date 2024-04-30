const fs = require('fs')

const rawPrettierRC = fs.readFileSync(require.resolve('./.prettierrc'), {encoding: 'utf-8'})
const prettierConfig = JSON.parse(rawPrettierRC)

// module.exports = {
//   root: true,
//   env: { browser: true, es2020: true },
//   extends: [
//     'eslint:recommended',
//     'plugin:@typescript-eslint/recommended',
//     'plugin:react-hooks/recommended',
//   ],
//   ignorePatterns: ['dist', '.eslintrc.cjs'],
//   parser: '@typescript-eslint/parser',
//   plugins: ['react-refresh'],
//   rules: {
//     'react-refresh/only-export-components': [
//       'warn',
//       { allowConstantExport: true },
//     ],
//   },
// }

module.exports = {
  root: true,
  env: {browser: true, es2020: true},
  parser: '@typescript-eslint/parser',
  settings: {
    react: {
      version: 'detect',
    },
    'import/resolver': {
      typescript: {},
    },
  },
  plugins: ['typescript-sort-keys', 'sort-export-all', 'unused-imports', 'react-refresh'],
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:jsx-a11y/recommended',
    'plugin:react/recommended',
    'plugin:react-hooks/recommended',
    'plugin:import/errors',
    'plugin:import/warnings',
    'plugin:import/typescript',
    'plugin:promise/recommended',
    'plugin:prettier/recommended',
  ],
  rules: {
    'prettier/prettier': ['error', prettierConfig],
    '@typescript-eslint/consistent-type-imports': 'error',
    '@typescript-eslint/explicit-module-boundary-types': 'off',
    '@typescript-eslint/no-unused-vars': 'off',
    '@typescript-eslint/camelcase': 0,
    '@typescript-eslint/no-extra-semi': 0,
    '@typescript-eslint/explicit-function-return-type': 0,
    '@typescript-eslint/no-explicit-any': 2,
    'import/no-duplicates': 'error',
    'no-empty': ['error', {allowEmptyCatch: true}],
    'no-restricted-syntax': ['error'],
    'react/button-has-type': ['error'],
    'react/jsx-curly-brace-presence': ['error', {props: 'never', children: 'never'}],
    'react/no-unescaped-entities': ['error', {forbid: ['>', '}']}],
    'react/prop-types': ['error', {skipUndeclared: true}],
    'react/react-in-jsx-scope': 'off',
    'require-await': 'error',
    'react-hooks/rules-of-hooks': 'error',
    'react-hooks/exhaustive-deps': [
      'error',
      {
        additionalHooks: '(useAsyncEffect)',
      },
    ],
    'unused-imports/no-unused-imports': 'error',
    'unused-imports/no-unused-vars': [
      'error',
      {vars: 'all', varsIgnorePattern: '^_', args: 'after-used', argsIgnorePattern: '^_'},
    ],
    // https://github.com/benmosher/eslint-plugin-import/blob/master/docs/rules/order.md
    'import/order': [
      'error',
      {
        'newlines-between': 'always',
        pathGroupsExcludedImportTypes: [],
        groups: ['builtin', 'external', 'internal', 'object', 'parent', 'sibling', 'index', 'unknown'],
        pathGroups: [
          {
            pattern: './*.css',
            group: 'index',
          },
          {
            pattern: './*.types',
            group: 'index',
          },
          {
            pattern: './*.constants',
            group: 'index',
          },
        ],
        alphabetize: {
          order: 'asc',
          caseInsensitive: true,
        },
      },
    ],
    'no-restricted-imports': [
      'error',
      {
        name: 'lodash-es',
        message: 'Please use lodash instead - https://nda.ya.ru/t/AyGjCGpx5K2Ni5',
      },
    ],
    'sort-export-all/sort-export-all': 'error',
    'import/no-extraneous-dependencies': [
      'error',
      {
        packageDir: './',
      },
    ],
  },
  overrides: [
    {
      files: ['*.js'],
      rules: {
        '@typescript-eslint/no-var-requires': 'off',
      },
    },
    {
      files: ['**/*.{ts,tsx}'],
      parserOptions: {
        project: './tsconfig.json',
      },
      rules: {
        '@typescript-eslint/no-floating-promises': 'error',
        '@typescript-eslint/no-misused-promises': ['error'],
      },
    },
  ],
  ignorePatterns: ['**/node_modules/*', '**/dist/*', '**/.eslintrc.cjs', '**/vite.config.ts'],
}
