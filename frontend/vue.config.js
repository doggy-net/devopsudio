const path = require('path');
module.exports = {
  chainWebpack: config => {
    const svgRule = config.module.rule('svg')
    svgRule.uses.clear()
  },
  configureWebpack: {
    module: {
      rules: [
        {
          test: /\.svg$/,
          loader: 'svg-sprite-loader',
          include: [path.resolve('src/components/Icon/svg-icons')],
          options: {
            symbolId: 'icon-[name]',
            limit: 10000
          }
        },
        {
          test: /\.svg$/,
          loader: 'file-loader',
          exclude: [path.resolve('src/components/Icon/svg-icons')],
          options: {
            name: 'img/[name].[hash:8].[ext]',
            limit: 10000
          }
        }
      ]
    }
  },
  devServer: {
    proxy: 'http://localhost:8000'
  }
}
