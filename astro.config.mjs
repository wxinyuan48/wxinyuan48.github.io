import { defineConfig } from "astro/config";

const [owner, repository] = (process.env.GITHUB_REPOSITORY || "/").split("/");
const isUserSite = repository === `${owner}.github.io`;

export default defineConfig({
  site: owner ? `https://${owner}.github.io` : "http://localhost:4321",
  base: process.env.GITHUB_ACTIONS && !isUserSite ? `/${repository}` : "/",
  output: "static",
  build: { assets: "_assets" },
  vite: {
    build: { target: "es2022" },
  },
});
