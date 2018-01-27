const path = require('path')
const ExtractTextPlugin = require('extract-text-webpack-plugin')
const webpack = require('webpack')
const BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  context: __dirname,
  entry: {
    'js/app.js': './frontend/assets/js/app.js',
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
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },
      {
        test: /\.vue?$/,
        exclude: /node_modules/,
        loader: 'vue-loader',
        options: {
          esModule: true,
          optimizeSSR: false
        },
      },
    ],
  },
  plugins: [
    new ExtractTextPlugin('[name]'),
    new BundleTracker({filename: './webpack-stats.json'}),
  ],
}
