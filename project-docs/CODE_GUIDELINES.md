# CODE_GUIDELINES.md

---

## Part 1: Core Philosophy

### **KISS (Keep It Simple, Stupid)**
*   **Principle:** Simplicity is a primary goal. Avoid unnecessary complexity. Always favor the most straightforward solution that is correct, robust, and maintainable.
*   **Application:** When presented with multiple ways to solve a problem, default to the one that is easiest to read, understand, and debug. Resist the urge to use overly "clever" or obscure language features if a simpler approach will suffice.

### **DRY (Don't Repeat Yourself)**
*   **Principle:** Every piece of knowledge or logic in the system must have a single, unambiguous, authoritative representation.
*   **Application:** If you find yourself writing the same lines of code in multiple places, stop and abstract that logic into a reusable function, class, or component. This applies to documentation and scripts as well as source code.

### **YAGNI (You Aren't Gonna Need It)**
*   **Principle:** Do not add functionality until it is explicitly required by the Product Requirements Document (`PRD.md`).
*   **Application:** Resist adding speculative features, configuration options, or architectural layers based on what *might* be needed in the future. Focus entirely on delivering the simplest possible solution for the current, concrete requirements.

---

## Part 2: The SOLID Principles

SOLID is a set of five design principles for creating understandable, flexible, and maintainable object-oriented software.

### **1. SRP (Single Responsibility Principle)**
*   **Principle:** A class or module should have one, and only one, reason to change.
*   **Application:** Every component should have a single, well-defined purpose. For example, a module that fetches data from an API should not also be responsible for rendering that data in the UI. Keep data transformation, business logic, and presentation in separate, focused units.

### **2. OCP (Open/Closed Principle)**
*   **Principle:** Software entities (classes, modules, functions) should be open for extension, but closed for modification.
*   **Application:** Design components so that new functionality can be added with minimal changes to existing code. In Rust, this is often achieved with traits. In React, this can be achieved with component composition or plugin architectures. For example, to add a new map layer, you should be able to create a new layer component without altering the core map container.

### **3. LSP (Liskov Substitution Principle)**
*   **Principle:** Subtypes must be completely substitutable for their base types without altering the correctness of the program.
*   **Application:** When using inheritance or implementing traits/interfaces, ensure the subclass or implementation honors the contract of the base type. It should not throw new exceptions or have surprising side effects that the base contract does not specify.

### **4. ISP (Interface Segregation Principle)**
*   **Principle:** Clients should not be forced to depend on interfaces they do not use. Prefer many small, specific interfaces over one large, "fat" interface.
*   **Application:** Keep interfaces (or Rust traits) minimal and focused on a single behavior. For example, instead of a single `IDataHandler` trait with `read`, `write`, and `delete` methods, it might be better to have separate `IDataReader` and `IDataWriter` traits for clients that only need one of those capabilities.

### **5. DIP (Dependency Inversion Principle)**
*   **Principle:** High-level modules should not depend on low-level modules; both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions.
*   **Application:** This is the core of a "pluggable" architecture. A high-level component (e.g., a React page) should not depend directly on a concrete data-fetching implementation (e.g., a specific `fetchUgaritData` function). Instead, it should depend on an abstraction (e.g., a `useData` hook or a `IDataService` interface), and the concrete implementation can be provided via dependency injection. This makes components easier to test and reuse.

---

## Part 3: User-Facing Principles

### **POLA (Principle of Least Astonishment)**
*   **Principle:** A component or system should behave in a way that most users (including developers using its API) will expect it to behave. Its behavior should not be surprising.
*   **Application:**
    *   **API Design:** A function named `getUser()` should return a user; it should not also delete a temporary file as a side effect.
    *   **UI/UX:** Clicking a "Save" button should save the current state; it shouldn't also navigate to a different page unexpectedly.
    *   **Encapsulation:** This is directly related to the concept of a **"short interface, a lot of depth."** Hide complex internal workings behind a simple, predictable public API. The caller shouldn't need to know the implementation details to use it correctly.