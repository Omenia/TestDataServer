'use strict'
const path = require('path')

module.exports = {
  build: {
    // Templates
    dashboard: path.resolve(__dirname, '../../server/templates/dashboard.html'),
    configuration: path.resolve(__dirname, '../../server/templates/configuration.html'),
    settings: path.resolve(__dirname, '../../server/templates/settings.html'),

    // Paths
    assetsRoot: path.resolve(__dirname, '../../server/static'),
    assetsSubDirectory: '',
    assetsPublicPath: '/static',

    /**
     * Source Maps
     */

    productionSourceMap: true,
    // https://webpack.js.org/configuration/devtool/#production
    devtool: '#source-map',

    // Gzip off by default as many popular static hosts such as
    // Surge or Netlify already gzip all static assets for you.
    // Before setting to `true`, make sure to:
    // npm install --save-dev compression-webpack-plugin
    productionGzip: false,
    productionGzipExtensions: ['js', 'css'],
  }
}
