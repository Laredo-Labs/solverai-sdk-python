# Changelog

## 0.1.0-alpha.6 (2025-07-25)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/Laredo-Labs/solverai-sdk-python/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Features

* clean up environment call outs ([c042cab](https://github.com/Laredo-Labs/solverai-sdk-python/commit/c042cab164591713caf3fddedf1a4cd0eecb318b))
* **client:** add follow_redirects request option ([c95346d](https://github.com/Laredo-Labs/solverai-sdk-python/commit/c95346d54d8de3668375c8be3b11b42da4c6c57e))
* **client:** add support for aiohttp ([ae63fa8](https://github.com/Laredo-Labs/solverai-sdk-python/commit/ae63fa80bb13fc414a233c9de700d697f1aa2939))


### Bug Fixes

* **ci:** correct conditional ([6d7672d](https://github.com/Laredo-Labs/solverai-sdk-python/commit/6d7672d2b9c01ff24cbae81a6224f8f50a294d67))
* **ci:** release-doctor — report correct token name ([f4cbba9](https://github.com/Laredo-Labs/solverai-sdk-python/commit/f4cbba90a637aa050bf574d65c3a1dcf09bd4cb2))
* **client:** correctly parse binary response | stream ([afb303a](https://github.com/Laredo-Labs/solverai-sdk-python/commit/afb303ae063e9b7a33cba3c6027e193319d6ff2e))
* **client:** don't send Content-Type header on GET requests ([8498952](https://github.com/Laredo-Labs/solverai-sdk-python/commit/849895238af82e081a6cb12ad25261dc9a8065c5))
* **parsing:** correctly handle nested discriminated unions ([65b2fce](https://github.com/Laredo-Labs/solverai-sdk-python/commit/65b2fcee7f88b55af930fa8194716f0c44229290))
* **parsing:** ignore empty metadata ([c7b7604](https://github.com/Laredo-Labs/solverai-sdk-python/commit/c7b7604b5dad423fd7a37dc33b6bee3c582b6ef1))
* **parsing:** parse extra field types ([700d455](https://github.com/Laredo-Labs/solverai-sdk-python/commit/700d45591cb4f6873702617aa496726ba0de56e3))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([9c10420](https://github.com/Laredo-Labs/solverai-sdk-python/commit/9c104203d955bd80a61ed8f7b9b1624effeeb722))


### Chores

* **ci:** change upload type ([bd43fa1](https://github.com/Laredo-Labs/solverai-sdk-python/commit/bd43fa10bcb7408bf9f96466b583881933add46c))
* **ci:** enable for pull requests ([c079ebc](https://github.com/Laredo-Labs/solverai-sdk-python/commit/c079ebc8d1e807a3ca8bc6af241eb30dc5d5ffca))
* **ci:** only run for pushes and fork pull requests ([8f32b36](https://github.com/Laredo-Labs/solverai-sdk-python/commit/8f32b36f84635831d9b57fda36b29f32ec63b31e))
* **docs:** remove reference to rye shell ([b72bf2d](https://github.com/Laredo-Labs/solverai-sdk-python/commit/b72bf2decfa2de0939062186a61db6c51c420c74))
* **internal:** bump pinned h11 dep ([72da51f](https://github.com/Laredo-Labs/solverai-sdk-python/commit/72da51f225f99ecb4989343344804ef31ac07c2c))
* **internal:** codegen related update ([a28bd38](https://github.com/Laredo-Labs/solverai-sdk-python/commit/a28bd389b016785fd1a7bb930d530d69c65b27c5))
* **internal:** update conftest.py ([a218d78](https://github.com/Laredo-Labs/solverai-sdk-python/commit/a218d788fc14ecdc32a554fa3982c585527377f7))
* **package:** mark python 3.13 as supported ([55eadd3](https://github.com/Laredo-Labs/solverai-sdk-python/commit/55eadd3c32b3c644b3d88a476db456efa7361a23))
* **project:** add settings file for vscode ([0c95966](https://github.com/Laredo-Labs/solverai-sdk-python/commit/0c9596692822dfe7679c4720b986dc283bcf07d4))
* **readme:** fix version rendering on pypi ([2298710](https://github.com/Laredo-Labs/solverai-sdk-python/commit/2298710b58eef2b1de92d0220fd9f6266f9998e5))
* **readme:** update badges ([634dc80](https://github.com/Laredo-Labs/solverai-sdk-python/commit/634dc806aa4109a5e061fe9ee8b3bfd6271c24c8))
* **tests:** add tests for httpx client instantiation & proxies ([5b7d79c](https://github.com/Laredo-Labs/solverai-sdk-python/commit/5b7d79cf7c8e982d206b4644994b951aaf8b6ba6))
* **tests:** run tests in parallel ([e7ef8cb](https://github.com/Laredo-Labs/solverai-sdk-python/commit/e7ef8cbffcc14a38c8c61cdd528bd0d5f3b2fded))
* **tests:** skip some failing tests on the latest python versions ([7b4f891](https://github.com/Laredo-Labs/solverai-sdk-python/commit/7b4f8919840448fdf9968e6eda9c9164eb8bec3e))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([40eb1f0](https://github.com/Laredo-Labs/solverai-sdk-python/commit/40eb1f0968839d3e384fdbcf41ac33fdf7f8b3de))

## 0.1.0-alpha.5 (2025-05-28)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/Laredo-Labs/solverai-sdk-python/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

* **api:** api update ([fbb59a0](https://github.com/Laredo-Labs/solverai-sdk-python/commit/fbb59a03fe9493129ab3aa21ec141a5cc212ddba))
* **api:** change localization APIs ([fd816ad](https://github.com/Laredo-Labs/solverai-sdk-python/commit/fd816ad449ebd4a5854cc6ec87ec4d38c2da53d1))


### Bug Fixes

* **package:** support direct resource imports ([10e8f06](https://github.com/Laredo-Labs/solverai-sdk-python/commit/10e8f0654a7cbaef8904555ccc00d8a142a03071))


### Chores

* **ci:** fix installation instructions ([7c030e9](https://github.com/Laredo-Labs/solverai-sdk-python/commit/7c030e945fecfbefc52efd57c9c598741b7d3d53))
* **ci:** upload sdks to package manager ([1cf1dda](https://github.com/Laredo-Labs/solverai-sdk-python/commit/1cf1ddab93b0aa92ccae0979ef2f66c5fb6f6b4c))
* **docs:** grammar improvements ([c1f9854](https://github.com/Laredo-Labs/solverai-sdk-python/commit/c1f98549dcaf2865c26d4b07489998aeae4aefdb))
* **docs:** use Sandbox repo in examples ([79947e1](https://github.com/Laredo-Labs/solverai-sdk-python/commit/79947e1bf4459bd74741e1a06f9eb95a1df8d29b))
* **internal:** avoid errors for isinstance checks on proxies ([52844ce](https://github.com/Laredo-Labs/solverai-sdk-python/commit/52844ce238bf470cb1fb252ec0ddd5787132a5f3))
* **internal:** codegen related update ([d3194a5](https://github.com/Laredo-Labs/solverai-sdk-python/commit/d3194a52b6781fbc8c1f00839b9650090ce6f3f1))

## 0.1.0-alpha.4 (2025-04-29)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/Laredo-Labs/solverai-sdk-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** added wait_for_completion methods ([3b6633d](https://github.com/Laredo-Labs/solverai-sdk-python/commit/3b6633d9f252d84e4e33ce8e92be979d0c74068e))
* **api:** api update ([d1d07c5](https://github.com/Laredo-Labs/solverai-sdk-python/commit/d1d07c5c7040742ea0bf22e439987441289f528e))
* **api:** introduce create_and_solve methods ([43006c3](https://github.com/Laredo-Labs/solverai-sdk-python/commit/43006c3ab5d11305016b56b1db0fdd0ab2121894))

## 0.1.0-alpha.3 (2025-04-25)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/Laredo-Labs/solverai-sdk-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** api update ([3ba1eb7](https://github.com/Laredo-Labs/solverai-sdk-python/commit/3ba1eb75634c8475c28b6eccd20828cffe6a1611))
* **api:** remove vestigial endpoint declarations ([04dba71](https://github.com/Laredo-Labs/solverai-sdk-python/commit/04dba719b87894e58fb9de83365e74fe3b175aff))

## 0.1.0-alpha.2 (2025-04-25)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/Laredo-Labs/solverai-sdk-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** api update ([4115e3f](https://github.com/Laredo-Labs/solverai-sdk-python/commit/4115e3f2a2d8978b203e6a92f734df4303883f25))
* **api:** api update ([49ac631](https://github.com/Laredo-Labs/solverai-sdk-python/commit/49ac6314404d014dcc427e916d99e78a67ef5824))


### Documentation

* **api:** fix docs link, update support contact ([bf540c3](https://github.com/Laredo-Labs/solverai-sdk-python/commit/bf540c33f6077c86047e806ded46e9655cd8457a))

## 0.1.0-alpha.1 (2025-04-25)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/Laredo-Labs/solverai-sdk-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([3581c64](https://github.com/Laredo-Labs/solverai-sdk-python/commit/3581c640b87cbe289efc4a7a08564a9ae411ca17))
* **api:** update via SDK Studio ([306cbd8](https://github.com/Laredo-Labs/solverai-sdk-python/commit/306cbd83a940dfe4b7ea7b5409942a9dd5ba033f))
* **api:** update via SDK Studio ([1e2eea0](https://github.com/Laredo-Labs/solverai-sdk-python/commit/1e2eea06cb5dc8c8064b4b270348f1314e8f888a))
* **api:** update via SDK Studio ([c4f07d8](https://github.com/Laredo-Labs/solverai-sdk-python/commit/c4f07d87fe333341decfc944f40ae50079b9f101))


### Bug Fixes

* **pydantic v1:** more robust ModelField.annotation check ([fb446a4](https://github.com/Laredo-Labs/solverai-sdk-python/commit/fb446a49433f676c32ed09594f436321db9f4fa3))


### Chores

* broadly detect json family of content-type headers ([8c7adce](https://github.com/Laredo-Labs/solverai-sdk-python/commit/8c7adced1025f48a09cc60f2192a389ae3cc0b57))
* **ci:** add timeout thresholds for CI jobs ([747d18f](https://github.com/Laredo-Labs/solverai-sdk-python/commit/747d18fec846fc3b1796be0cfb2a91a90683263b))
* **ci:** only use depot for staging repos ([0e13fdf](https://github.com/Laredo-Labs/solverai-sdk-python/commit/0e13fdfa795b2ceef2e7e242aa2c0d26ab0756ea))
* go live ([63ea47d](https://github.com/Laredo-Labs/solverai-sdk-python/commit/63ea47d9b6f641ff2779ea928839e7d2576f3a67))
* go live ([269266e](https://github.com/Laredo-Labs/solverai-sdk-python/commit/269266e5853b734ce774bd8660151d61bcb5337a))
* **internal:** codegen related update ([1f20bad](https://github.com/Laredo-Labs/solverai-sdk-python/commit/1f20badfb0ade74ed54828da3b702b369d4bcd71))
* **internal:** fix list file params ([22afcc8](https://github.com/Laredo-Labs/solverai-sdk-python/commit/22afcc855f286278595458214ad8ceca0d52f0a7))
* **internal:** import reformatting ([0e1374c](https://github.com/Laredo-Labs/solverai-sdk-python/commit/0e1374c790a7716b399cf597d826590aa18bf06e))
* **internal:** refactor retries to not use recursion ([4020e02](https://github.com/Laredo-Labs/solverai-sdk-python/commit/4020e0289602a18e861fe800a72937b46236fdad))
* update SDK settings ([99c7592](https://github.com/Laredo-Labs/solverai-sdk-python/commit/99c7592daee266b1807f019bd7d16d74e60d9379))
