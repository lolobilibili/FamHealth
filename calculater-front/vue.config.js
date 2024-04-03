
const {defineConfig} = require('@vue/cli-service')

module.exports = defineConfig({
    transpileDependencies: true,
    lintOnSave: false,
    assetsDir: 'static',
    // devServer: {
    //     // 指定使用的ip地址，默认为localhost，如果使用'0.0.0.0'则可以被外部访问
    //     host: '0.0.0.0',
    //     // 指定服务监听的端口号
    //     port: 9527,
    //     // 代理
    //     proxy: {
    //         [process.env.VUE_APP_BASE_API]: {
    //             target: 'http://localhost:8080',
    //             changeOrigin: true,
    //             pathRewrite: {
    //                 ['^' + process.env.VUE_APP_BASE_API]: ''
    //             }
    //         }
    //     }
    // }
    devServer: {
      open:true,
      host:'localhost',
      port: 80,
      https: false
    }
})
