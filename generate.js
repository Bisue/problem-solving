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

function getProblemInfo(site, level, problem) {
  const realPath = path.resolve(".", site, level, problem);

  return {
    title: fs
      .readFileSync(realPath)
      .toString()
      .split("\n")[0]
      .replace(/^(\/\/|\#)/g, "")
      .trim(),
    href: `/${site}/${level}/${problem}`,
  };
}

function getLevelInfo(site, level) {
  const realPath = path.resolve(".", site, level);

  return fs
    .readdirSync(realPath)
    .filter((p) => !ignores.includes(p))
    .map((p) => getProblemInfo(site, level, p));
}

function getSiteInfo(site) {
  const levels = Object.keys(siteMeta[site]);
  const realPath = path.resolve(".", site);

  return fs
    .readdirSync(realPath)
    .filter((d) => levels.includes(d))
    .reduce(
      (acc, l) => ({
        ...acc,
        [siteMeta[site][l]]: getLevelInfo(site, l),
      }),
      {}
    );
}

function buildProblemsMarkdown(solvedProblems, site, level) {
  return solvedProblems[site][level]
    .map((p) => `- [${p.title}](${p.href})`)
    .join("\n  ");
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

const siteNames = Object.keys(siteMeta);

const siteDirectories = fs
  .readdirSync(path.resolve("."))
  .filter((d) => siteNames.includes(d));

const solvedProblems = siteDirectories.reduce((acc, site) => {
  const problems = getSiteInfo(site);

  return {
    ...acc,
    [site]: problems,
  };
}, {});

fs.writeFileSync(path.resolve(".", output), buildMarkdown(solvedProblems));

console.log(`${output} 생성이 완료되었습니다.`);
