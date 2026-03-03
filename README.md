<p align="center"><strong>McCoy R. Becker (femtomc)</strong></p>
<p align="center"><a href="https://femtomc.github.io">Homepage</a> · <a href="https://github.com/femtomc">GitHub</a> · <a href="https://github.com/femtomc/genjax">GenJAX</a> · <a href="https://probcomp.csail.mit.edu/">MIT ProbComp</a></p>

<img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=femtomc&theme=github_dark" align="right" width="40%" />

I’m a parent and a PhD researcher at MIT ProbComp.

I work on probabilistic algorithms and software for modern hardware, with a lot of time spent in programming languages, compilers, and agent tooling.

Current focus:

- probabilistic programming on accelerators
- programmable inference systems
- long-running operator workflows for reliable agents

<br clear="right"/>

### Selected long-running projects

_This list prioritizes projects with sustained multi-week development and omits short scratch repos._

#### Probabilistic programming

- **[genjax](https://github.com/femtomc/genjax)** — Probabilistic programming language built on JAX, centered on **generative functions** and **traces**; supports programmable Monte Carlo + variational inference workflows, and is packaged as a POPL'26 artifact with docs/tests/case studies. <img align="right" alt="stars" src="https://img.shields.io/github/stars/femtomc/genjax?style=social" />
- **[programmable-vi-pldi-2024](https://github.com/femtomc/programmable-vi-pldi-2024)** — Artifact repository for the PLDI 2024 paper _Probabilistic programming with programmable variational inference_; includes the JAX implementation plus reproducibility scripts for the evaluation figures/tables. <img align="right" alt="stars" src="https://img.shields.io/github/stars/femtomc/programmable-vi-pldi-2024?style=social" />
- **[Jaynes.jl](https://github.com/femtomc/Jaynes.jl)** — Research-oriented alpha DSL/compiler for probabilistic programming in Julia; uses source-to-source IR transformations and contextual dispatch to implement the Gen.jl generative function interface. <img align="right" alt="stars" src="https://img.shields.io/github/stars/femtomc/Jaynes.jl?style=social" />
- **[Problox.jl](https://github.com/femtomc/Problox.jl)** — Julia DSL for probabilistic logic programming that wraps ProbLog; compiles Julia-side model syntax into ProbLog programs and supports direct evaluation/querying from Julia. <img align="right" alt="stars" src="https://img.shields.io/github/stars/femtomc/Problox.jl?style=social" />

#### Language and compiler systems

- **[abstraps](https://github.com/femtomc/abstraps)** — Rust compiler framework for extensible abstract interpretation, with MLIR-isomorphic IR concepts, abstract-VM interpreter interfaces, and builders for MLIR code generation. <img align="right" alt="stars" src="https://img.shields.io/github/stars/femtomc/abstraps?style=social" />
- **[juju](https://github.com/femtomc/juju)** — Extensible compiler from JAX computations (Jaxprs) to Modular MAX graphs; lowers JAX primitives to MAX operations for execution in MAX inference sessions. <img align="right" alt="stars" src="https://img.shields.io/github/stars/femtomc/juju?style=social" />
- **[pistachio](https://github.com/femtomc/pistachio)** — Experimental dependently typed language/theorem-prover implementation focused on elaboration and normalization-by-evaluation techniques. <img align="right" alt="stars" src="https://img.shields.io/github/stars/femtomc/pistachio?style=social" />

#### Agent tooling

- **[mu](https://github.com/femtomc/mu)** — Programmable personal assistant for technical work, designed for long-running execution/persistence/reactivity; exposes shell-first primitives (issues, heartbeats, programmable `mu_ui` docs) for custom orchestration. <img align="right" alt="stars" src="https://img.shields.io/github/stars/femtomc/mu?style=social" />

---

<p align="center">
  <a href="https://femtomc.github.io">femtomc.github.io</a>
</p>
