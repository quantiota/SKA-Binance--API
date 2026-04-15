
## Binary Transition Space


We believe—like John Archibald Wheeler—that the ultimate foundation of reality is information:

> “It from bit symbolizes the idea that every item of the physical world has at bottom—a very deep bottom, in most instances—an immaterial source and explanation; that what we call reality arises, in the last analysis, from the posing of yes-no questions and the registering of equipment-evoked responses; in short, that all things physical are information-theoretic in origin and that this is a participatory universe.”

*John Archibald Wheeler, “Information, Physics, Quantum: The Search for Links” (1989/1990).*


---

## State Encoding

The 3 regime states are encoded as 2-bit binary values:

| State   | Code |
|---------|------|
| neutral | `00` |
| bull    | `01` |
| bear    | `10` |

Code `11` is undefined and never occurs.

---

## Transition Encoding

A transition A→B is a **4-bit word**: `[a₁, a₀, b₁, b₀]` (from-state | to-state).

This grounds all transitions in binary arithmetic and makes AND/OR/XOR operations well-defined.

| Transition       | From | To   | 4-bit word |
|-----------------|------|------|------------|
| neutral→neutral | `00` | `00` | `0000`     |
| neutral→bull    | `00` | `01` | `0001`     |
| neutral→bear    | `00` | `10` | `0010`     |
| bull→neutral    | `01` | `00` | `0100`     |
| bull→bull       | `01` | `01` | `0101`     |
| bull→bear       | `01` | `10` | `0110`     |
| bear→neutral    | `10` | `00` | `1000`     |
| bear→bull       | `10` | `01` | `1001`     |
| bear→bear       | `10` | `10` | `1010`     |

---

## The 9-Dimensional Binary Transition Space

In the SKA 3-state regime machine (bull, neutral, bear), there are 9 possible transition types. Each transition is a **yes/no question** — a single bit of information.

The 9 basis transitions, indexed by their 4-bit word, each with its one-hot vector `e_t ∈ {0,1}⁹`:

| Index | Transition       | 4-bit word |
|-------|-----------------|------------|
| 0     | neutral→neutral | `0000`     |
| 1     | neutral→bull    | `0001`     |
| 2     | neutral→bear    | `0010`     |
| 3     | bull→neutral    | `0100`     |
| 4     | bear→neutral    | `1000`     |
| 5     | bull→bear       | `0110`     |
| 6     | bear→bull       | `1001`     |
| 7     | bull→bull       | `0101`     | — never observed |
| 8     | bear→bear       | `1010`     | — never observed |

---

## Binary Vector of a Sequence

Given a sequence of transitions `S = (t₁, t₂, ..., tₙ)`, its binary vector is the **bitwise OR of all one-hot vectors**:

```
bv(S) = e_t1 OR e_t2 OR ... OR e_tn
```

Each bit answers: *"did this transition type appear at least once in the sequence?"*

This maps every sequence to a point in `{0,1}⁹` — the binary transition space.

---

## Composition Operator ∘

Two transitions compose if the **to-state** of the first equals the **from-state** of the second:

```
t₁ ∘ t₂  is valid  iff  lower_2_bits(t₁) == upper_2_bits(t₂)
```

The result is the transition from the from-state of `t₁` to the to-state of `t₂`:

```
t₁ ∘ t₂ = (t₁ AND 1100) OR (t₂ AND 0011)
```

Example:

```
neutral→neutral ∘ neutral→bull
= (0000 AND 1100) OR (0001 AND 0011)
= 0000 OR 0001
= 0001  (neutral→bull)  ✓
```

This is the **grammar rule** of the binary transition space. A sequence `(t₁, t₂, ..., tₙ)` is grammatically valid if and only if every consecutive pair composes — the intermediate states cancel out.

---

## AND as the Matching Operator

A live sequence `S` **contains** a false start pattern `P` if and only if:

```
bv(S) AND bv(P) == bv(P)
```

The AND gate asks: *"does the sequence activate every bit required by the pattern?"*

This is the detection rule used against the false start library.

---

## Example — Case 12

Sequence: `neutral→bear, bear→neutral, neutral→bull, bull→neutral, neutral→bear, bear→bull, bull→neutral`

4-bit words present:

| Transition       | 4-bit word | Index |
|-----------------|------------|-------|
| neutral→neutral | `0000`     | 0     |
| neutral→bear    | `0010`     | 2     |
| bear→neutral    | `1000`     | 4     |
| neutral→bull    | `0001`     | 1     |
| bull→neutral    | `0100`     | 3     |
| bear→bull       | `1001`     | 6     |
| bull→bear       | `0110`     | 5     | ← never appears → bit 5 = 0

```
bv = [1, 1, 1, 1, 1, 0, 1, 0, 0]
```
