const fs = require("fs");
const path = require("path");

// =================================================

const siteMeta = {
  programmers: {
    lv2: "레벨 2",
    lv3: "레벨 3",
  },
  baekjoon: {
    silver: "실버",
    gold: "골드",
  },
};
const ignores = [".gitkeep"];
const output = "solved.md";

// =================================================

const siteNames = Object.keys(siteMeta);

const siteDirectories = fs
  .readdirSync(path.resolve("."))
  .filter((d) => siteNames.includes(d));

const solvedProblems = siteDirectories.reduce((acc, site) => {
  const levels = Object.keys(siteMeta[site]);
  const problems = fs
    .readdirSync(path.resolve(".", site))
    .filter((d) => levels.includes(d))
    .reduce(
      (acc, l) => ({
        ...acc,
        [siteMeta[site][l]]: fs
          .readdirSync(path.resolve(".", site, l))
          .filter((p) => !ignores.includes(p))
          .map((p) => ({
            title: fs
              .readFileSync(path.resolve(".", site, l, p))
              .toString()
              .split("\n")[0]
              .replace(/^(\/\/|\#)/g, "")
              .trim(),
            href: `/${site}/${l}/${p}`,
          })),
      }),
      {}
    );

  return {
    ...acc,
    [site]: problems,
  };
}, {});

function buildProblemsMarkdown(solvedProblems, site, level) {
  return solvedProblems[site][level]
    .map((p) => `- [${p.title}](${p.href})`)
    .join("\n\n  ");
}

function buildLevelsMarkdown(solvedProblems, site) {
  return Object.keys(solvedProblems[site])
    .map(
      (l) => `#### ${l}
    
  ${buildProblemsMarkdown(solvedProblems, site, l)}`
    )
    .join("\n\n  ");
}

function buildMarkdown(solvedProblems) {
  return Object.keys(solvedProblems)
    .map(
      (s) => `<details>
  <summary>${s}</summary>

  ${buildLevelsMarkdown(solvedProblems, s)}
</details>`
    )
    .join("\n\n");
}

fs.writeFileSync(path.resolve(".", output), buildMarkdown(solvedProblems));
