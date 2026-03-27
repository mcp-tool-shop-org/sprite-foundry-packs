#!/usr/bin/env node
/**
 * Verify all sprite packs in the monorepo.
 * Runs each pack's verify script and reports results.
 */
import { readdirSync, existsSync } from "fs";
import { join } from "path";
import { execSync } from "child_process";

const packagesDir = join(import.meta.dirname, "..", "packages");
const packs = readdirSync(packagesDir).filter((d) =>
  existsSync(join(packagesDir, d, "pack.json"))
);

let failed = 0;

for (const pack of packs) {
  const dir = join(packagesDir, pack);
  process.stdout.write(`\n  ${pack} ... `);
  try {
    execSync("npm run verify", { cwd: dir, stdio: "pipe" });
    process.stdout.write("OK\n");
  } catch (e) {
    process.stdout.write("FAIL\n");
    console.error(e.stderr?.toString() || e.message);
    failed++;
  }
}

console.log(`\n${packs.length} packs checked, ${failed} failed.`);
process.exit(failed > 0 ? 1 : 0);
