# Projects & Theses

<small>These are the topics we work on. The more specific you are about what you want to do or which topic you want to work in, the better, so please contact [Peter Thiemann](../team/thiemann.md) with your idea.</small>

<noscript>
<style>pre:has(code.language-mermaid) { display: none; }</style>
<img src="projects-graph.svg" alt="Graph of our research topics: theory (type systems, mechanized proofs) and application (concurrency analysis, compilers)" style="width:100%">
</noscript>

```mermaid
flowchart TD
  root([Root]) --> theory[Theory]
  root --> application[Application]

  theory --> ts[Type Systems]
  ts --> dt[Dependent Types]
  ts --> st[Session Types]
  ts --> pc[Process Calculi]
  ts --> gt[Gradual Types]

  theory --> mp[Mechanized Proofs]
  mp --> statics[Statics]
  statics --> tsafe[Type Safety]
  statics --> atc[Algorithmic Typing Completeness]
  statics --> its[Intrinsically Typed Syntax]
  mp --> semantics[Semantics]
  semantics --> df[Deadlock Freedom]
  semantics --> sim[Simulation]

  application --> ca[Concurrency Analysis]
  ca --> sa[Static Analysis]
  ca --> da[Dynamic Analysis]

  application --> comp[Compilers]
  comp --> cp[Compilation Pipeline]
  comp --> tc[Type Checkers]
  comp --> interp[Interpreters]

  classDef rootc fill:#444,stroke:#222,color:#fff
  classDef th fill:#dbeafe,stroke:#2563eb,color:#111
  classDef ap fill:#dcfce7,stroke:#16a34a,color:#111
  class root rootc
  class theory,ts,dt,st,pc,gt,mp,statics,tsafe,atc,its,semantics,df,sim th
  class application,ca,sa,da,comp,cp,tc,interp ap
```
