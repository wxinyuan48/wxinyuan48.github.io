# Wang Xinyuan Portfolio

王馨苑的个人博客与动态作品集。网站使用 Astro、Three.js 和 GSAP 构建，部署目标为 GitHub Pages，无需登录或后台。

## Local development

```bash
pnpm install
pnpm run dev
```

## GitHub Pages

1. 在 GitHub 创建公开仓库，将本目录推送到 `main` 分支。
2. 打开 `Settings > Pages`，将 Source 设为 `GitHub Actions`。
3. 推送后，`Deploy portfolio to GitHub Pages` 工作流会自动构建并发布。

项目仓库和 `username.github.io` 用户站点两种路径都已兼容。所有媒体资源保存在 `public/assets`，网站不依赖外部字体、图片 CDN、账号或数据库。

## Content notes

- Unity 项目暂未加入，后续建议放在独立路由并点击后加载。
- 发布前请在 About 区补充真实邮箱、社交账号和 PDF 下载链接。
- `shutu-full-web.mp4` 约 60 MB，只在用户打开完整影片时加载。
