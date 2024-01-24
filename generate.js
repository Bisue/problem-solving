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
  "2024-dgu-spring-camp": {
    "01": "1일차 - 시간 복잡도 & 문제 접근 방법",
    "02": "2일차 - 반복문을 활용한 완전탐색 1",
    "03": "3일차 - 반복문을 활용한 완전탐색 2",
    "04": "4일차 - DFS 1",
    "05": "5일차 - DFS 2",
    "06": "6일차 - BFS 1",
    "07": "7일차 - BFS 2",
    "08": "8일차 - 중간고사",
    "09": "9일차 - 그래프 1",
    "10": "10일차 - 그래프 2",
    "11": "11일차 - 이분탐색",
    "12": "12일차 - 정렬과 분할정복복",
    "13": "13일차 - 우선순위 큐",
    "14": "14일차 - 그리디",
    "15": "15일차 - 셋, 맵",
    "16": "16일차 - 동적 프로그래밍 1",
    "17": "17일차 - 동적 프로그래밍 2",
    "18": "18일차 - 기말고사",
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
