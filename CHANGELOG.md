# Changelog

## 0.1.0-beta.6 (2026-03-20)

Full Changelog: [v0.1.0-beta.5...v0.1.0-beta.6](https://github.com/deeptable-com/deeptable-python/compare/v0.1.0-beta.5...v0.1.0-beta.6)

### Bug Fixes

* sanitize endpoint path params ([f0a7e87](https://github.com/deeptable-com/deeptable-python/commit/f0a7e877fd807e5f19900eb189c02e355e706450))

## 0.1.0-beta.5 (2026-03-19)

Full Changelog: [v0.1.0-beta.4...v0.1.0-beta.5](https://github.com/deeptable-com/deeptable-python/compare/v0.1.0-beta.4...v0.1.0-beta.5)

### Chores

* ignore macOS .DS_Store ([f001928](https://github.com/deeptable-com/deeptable-python/commit/f001928bf35641c543265f7318089d004881f502))

## 0.1.0-beta.4 (2026-03-17)

Full Changelog: [v0.1.0-beta.3...v0.1.0-beta.4](https://github.com/deeptable-com/deeptable-python/compare/v0.1.0-beta.3...v0.1.0-beta.4)

### Bug Fixes

* **deps:** bump minimum typing-extensions version ([2ff69c1](https://github.com/deeptable-com/deeptable-python/commit/2ff69c1d377cbef6bf4a9641277dde8c24b2a69b))
* **pydantic:** do not pass `by_alias` unless set ([0e37c83](https://github.com/deeptable-com/deeptable-python/commit/0e37c835b61b29e912c106790e00997b4be9e0a8))


### Chores

* **api:** minor updates ([ad9326f](https://github.com/deeptable-com/deeptable-python/commit/ad9326f69976fc60b578298ceb833932cf586dd0))
* **ci:** bump uv version ([204f9d5](https://github.com/deeptable-com/deeptable-python/commit/204f9d5ee8e55b4377247b665790c0b5b8338e57))
* **ci:** skip uploading artifacts on stainless-internal branches ([4fd2dd5](https://github.com/deeptable-com/deeptable-python/commit/4fd2dd5ffd08a07b4605fea550ecc0d64a7d84ec))
* format all `api.md` files ([f4314a5](https://github.com/deeptable-com/deeptable-python/commit/f4314a5175a16b8427c1ee0376b4c7561a97d12b))
* **internal:** add request options to SSE classes ([4df5e12](https://github.com/deeptable-com/deeptable-python/commit/4df5e129245688ca89abc8b21bb8ece2f5315e94))
* **internal:** bump dependencies ([8de81c0](https://github.com/deeptable-com/deeptable-python/commit/8de81c067d8afa18f079419c4bff16986654b4b0))
* **internal:** codegen related update ([dc82876](https://github.com/deeptable-com/deeptable-python/commit/dc8287698edfb2d8d94221e173f15dd20087f1fb))
* **internal:** fix lint error on Python 3.14 ([86b7765](https://github.com/deeptable-com/deeptable-python/commit/86b7765ca61d862c9e8d3199beb17acbee2556bb))
* **internal:** make `test_proxy_environment_variables` more resilient ([61cd3a4](https://github.com/deeptable-com/deeptable-python/commit/61cd3a41d5f28295972b79fc4d343574abe588ff))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([134719a](https://github.com/deeptable-com/deeptable-python/commit/134719a29b9dd7f4b0a47711aae70cd13299b052))
* **internal:** remove mock server code ([8459400](https://github.com/deeptable-com/deeptable-python/commit/8459400cfe8426bbe32eb3081b9f400ab016655e))
* **internal:** tweak CI branches ([7043aad](https://github.com/deeptable-com/deeptable-python/commit/7043aad90e9503825527ed5a6b8a2d45478448ed))
* update mock server docs ([3383c79](https://github.com/deeptable-com/deeptable-python/commit/3383c7931f23aa4e445ccd1b6a8f4fc29e4de621))
* update placeholder string ([4cf041a](https://github.com/deeptable-com/deeptable-python/commit/4cf041ab16ff82196562cd656959be70703eddad))

## 0.1.0-beta.3 (2026-01-30)

Full Changelog: [v0.1.0-beta.2...v0.1.0-beta.3](https://github.com/deeptable-com/deeptable-python/compare/v0.1.0-beta.2...v0.1.0-beta.3)

### Features

* Add column_sqlite_type and column_parquet_type to ColumnMetadata and enhance metadata tracking ([5abadf1](https://github.com/deeptable-com/deeptable-python/commit/5abadf12772b4c73b8ff3e5401f38f90913e6ce2))

## 0.1.0-beta.2 (2026-01-30)

Full Changelog: [v0.1.0-beta.1...v0.1.0-beta.2](https://github.com/deeptable-com/deeptable-python/compare/v0.1.0-beta.1...v0.1.0-beta.2)

### Features

* Add 'metadata' to TableType enum ([c2b9e6f](https://github.com/deeptable-com/deeptable-python/commit/c2b9e6f5bc560ee5a3ff5b44121a0160f8ae6d3e))
* **client:** add custom JSON encoder for extended type support ([fa289e1](https://github.com/deeptable-com/deeptable-python/commit/fa289e16773cceab8a41e5b37853d7e98f55a38f))

## 0.1.0-beta.1 (2026-01-28)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-beta.1](https://github.com/deeptable-com/deeptable-python/compare/v0.1.0-alpha.4...v0.1.0-beta.1)

### Bug Fixes

* documentation inconsistencies ([deb388e](https://github.com/deeptable-com/deeptable-python/commit/deb388e79ae20c3a4bdf6e6a5ebbe732b32c3fc6))

## 0.1.0-alpha.4 (2026-01-27)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/deeptable-com/deeptable-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* Add seed_bill_snow.py to test.yaml for Bruno E2E tests ([6ae40ec](https://github.com/deeptable-com/deeptable-python/commit/6ae40ecffa73852845f5f7e679fc0f6524c6b439))
* Fix seed.sql to overwrite records on conflict ([3a766c7](https://github.com/deeptable-com/deeptable-python/commit/3a766c7cf55c336c2cb1d32015eaaf4d88f9786e))

## 0.1.0-alpha.3 (2026-01-26)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/deeptable-com/deeptable-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* Make format parameter required in download_table endpoint and improve OpenAPI spec publishing ([efb6258](https://github.com/deeptable-com/deeptable-python/commit/efb625837a2e6fe68e00a01a16147d00f6af0b6a))

## 0.1.0-alpha.2 (2026-01-26)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/deeptable-com/deeptable-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** add new routes for download_file and change structured-sheets endpoint to replace exports with tables subresource ([fd9db6c](https://github.com/deeptable-com/deeptable-python/commit/fd9db6c25ae5fff08367028f11417032d3910a08))
* Setup OpenAPI sync for SDK generation and implement new API routes ([7cdb575](https://github.com/deeptable-com/deeptable-python/commit/7cdb575d3d764fef9143bf7d5f34d32b91c4a8be))


### Chores

* **ci:** upgrade `actions/github-script` ([50c8e20](https://github.com/deeptable-com/deeptable-python/commit/50c8e201129f2b5414523fe39a11e67fa83c6aa7))

## 0.1.0-alpha.1 (2026-01-23)

Full Changelog: [v0.0.1...v0.1.0-alpha.1](https://github.com/deeptable-com/deeptable-python/compare/v0.0.1...v0.1.0-alpha.1)

### Features

* **api:** change casing for DeepTable class ([470c907](https://github.com/deeptable-com/deeptable-python/commit/470c907140848a8475722b79d3056b6aa6684aec))
* **api:** change pagination scheme ([3613ac5](https://github.com/deeptable-com/deeptable-python/commit/3613ac5a3692365d28dd464a638d8df5fc9f79bc))


### Chores

* update SDK settings ([fe8f650](https://github.com/deeptable-com/deeptable-python/commit/fe8f650bea07ecca7253054825864b61f5db7647))
* update SDK settings ([46bd257](https://github.com/deeptable-com/deeptable-python/commit/46bd257650a90cefc9452e4be91319a5cb92e0fa))
