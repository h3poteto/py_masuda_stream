const path = require('path')
const ExtractTextPlugin = require('extract-text-webpack-plugin')
const BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  context: __dirname,
  entry: {
    'js/app.js': './frontend/assets/js/app.js',
    'css/app.css': './frontend/assets/css/app.scss',
  },
  output: {
    path: path.resolve('./public/assets/'),
    filename: '[name]',
  },
  resolve: {
    extensions: ['*', '.css', '.scss', '.js', '.vue'],
    alias: {
      'vue$': 'vue/dist/vue.esm.js',
    },
    modules: [path.resolve(__dirname, './'), 'node_modules'],
  },
  module: {
    loaders: [
      {
        enforce: 'pre',
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'eslint-loader',
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },
      {
        test: /\.vue?$/,
        loader: 'vue-loader',
        options: {
          esModule: true,
          optimizeSSR: false
        },
      },
      {
        // scssはloaderを通した上でcssとして出力したいので，ExtractTextPluginを使う
        test: /\.scss$/,
        loader: ExtractTextPlugin.extract({ fallback: 'style-loader', use: 'css-loader!sass-loader' }),
      },
      {
        // element-uiが提供するtheme-chalkのcssはcss-moduleとしてjsに読ませたい
        // そのためcssに関してはcssとして出力しない
        test: /\.css$/,
        loader: ['style-loader', 'css-loader', 'sass-loader'],
      },
      {
        test: /\.(woff|woff2)(\?v=\d+\.\d+\.\d+)?$/,
        loader: 'url-loader?limit=10000&mimetype=application/font-woff',
      },
      {
        test: /\.ttf(\?v=\d+\.\d+\.\d+)?$/,
        loader: 'url-loader?limit=10000&mimetype=application/octet-stream',
      },
      {
        test: /\.eot(\?v=\d+\.\d+\.\d+)?$/,
        loader: 'file-loader',
      },
      {
        test: /\.svg(\?v=\d+\.\d+\.\d+)?$/,
        loader: 'url-loader?limit=10000&mimetype=image/svg+xml',
      },
      {
        test: /\.(jpg|png)$/,
        loader: 'url-loader',
      },
    ],
  },
  plugins: [
    new ExtractTextPlugin('[name]'),
    new BundleTracker({filename: './webpack-stats.json'}),
  ],
}
