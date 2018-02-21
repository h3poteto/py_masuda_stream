const path = require('path')
const ExtractTextPlugin = require('extract-text-webpack-plugin')
const BundleTracker = require('webpack-bundle-tracker')
const UglifyJsPlugin = require('uglifyjs-webpack-plugin')
const CopyWebpackPlugin = require('copy-webpack-plugin')

// eslint-disable-next-line no-undef
const production = process.env.NODE_ENV === 'production'
const filename = production ? '[name]-[hash]' : '[name]'

module.exports = {
  context: __dirname,
  entry: {
    'js/app': './frontend/assets/js/app.js',
    'css/app': './frontend/assets/css/app.js',
    'css/not_login': './frontend/assets/css/not_login.js',
  },
  output: {
    path: path.resolve('./public/assets/'),
    filename: `${filename}.js`,
  },
  cache: true,
  resolve: {
    extensions: ['*', '.css', '.scss', '.js', '.vue'],
    alias: {
      'vue$': 'vue/dist/vue.esm.js',
    },
    modules: [path.resolve(__dirname, './'), 'node_modules'],
  },
  module: {
    rules: [
      {
        enforce: 'pre',
        test: /\.js$/,
        exclude: /node_modules/,
        use: 'eslint-loader',
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: [
          'cache-loader',
          'babel-loader',
        ]
      },
      {
        test: /\.vue?$/,
        use: [
          { loader: 'cache-loader' },
          {
            loader: 'vue-loader',
            options: {
              esModule: true,
              optimizeSSR: false
            },
          }
        ]
      },
      {
        // scssはloaderを通した上でcssとして出力したいので，ExtractTextPluginを使う
        test: /\.scss$/,
        exclude: /node_modules/,
        use: ExtractTextPlugin.extract({ fallback: 'style-loader', use: 'cache-loader!css-loader!sass-loader' }),
      },
      {
        // element-uiが提供するtheme-chalkのcssはcss-moduleとしてjsに読ませたい
        // そのためcssに関してはcssとして出力しない
        test: /\.css$/,
        use: ['cache-loader', 'style-loader', 'css-loader', 'sass-loader'],
      },
      {
        test: /\.(woff|woff2)(\?v=\d+\.\d+\.\d+)?$/,
        use: 'url-loader?limit=10000&mimetype=application/font-woff',
      },
      {
        test: /\.ttf(\?v=\d+\.\d+\.\d+)?$/,
        use: 'url-loader?limit=10000&mimetype=application/octet-stream',
      },
      {
        test: /\.eot(\?v=\d+\.\d+\.\d+)?$/,
        use: 'file-loader',
      },
      {
        test: /\.svg(\?v=\d+\.\d+\.\d+)?$/,
        use: 'url-loader?limit=10000&mimetype=image/svg+xml',
      },
      {
        test: /\.(jpg|png)$/,
        use: 'url-loader',
      },
    ],
  },
  plugins: [
    new ExtractTextPlugin(`${filename}.css`),
    new BundleTracker({filename: './webpack-stats.json'}),
    new CopyWebpackPlugin([{ from: './frontend/assets/images', to: './images' }]),
    ...(
      production ? [
        new UglifyJsPlugin()
      ] : []
    ),
  ],
}
