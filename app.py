import streamlit as st
from together import Together

st.set_page_config(page_title="AI Notes Maker (Llama-3 via Together)", layout="wide")
st.title("📝 AI Notes Maker (Llama-3 via Together AI)")

with st.sidebar:
    st.header("Customize Your Notes")
    topic = st.text_input("Topic", value="Machine Learning")
    depth = st.selectbox("Depth", ["basic", "intermediate", "comprehensive"], index=2)
    include_examples = st.checkbox("Include Examples?", value=True)
    audience = st.selectbox("Audience", ["students", "professionals", "general"], index=1)
    api_key = st.text_input("Together API Key", type="password")
    submit = st.button("Generate Notes")
    example = st.button("Example Output")

EXAMPLE_NOTES = """
### FINAL NOTES:
**Comprehensive Educational Notes on Quantum Computing**

1. **Introduction to Quantum Computing**
Quantum computing leverages principles of quantum mechanics to process information in ways that classical computers cannot. Unlike classical bits (0 or 1), qubits can exist in superposition (both 0 and 1 simultaneously) and entanglement (correlated qubits that share states regardless of distance). This enables quantum computers to perform complex calculations exponentially faster for certain problems. The field is rooted in quantum theory, with foundational contributions from scientists like Erwin Schrödinger, Werner Heisenberg, and Richard Feynman.

**Key Principles:**
- Superposition: Qubits can be in multiple states until measured.
- Entanglement: Qubits can be linked such that the state of one instantly influences the other.
- Quantum Gates: Operations (e.g., Hadamard, CNOT) manipulate qubits, with reversible operations critical to quantum algorithms.

**Historical Context:**
- The 5th Solvay Conference (1927) marked the birth of quantum theory, with Nobel laureates like Feynman and Schrödinger.
- Google’s 2019 quantum supremacy claim (solving a 5,000-qubit problem in 200 seconds) demonstrated quantum advantage.

2. **Fundamental Concepts**
2.1 Qubits and Superposition  
Qubit Definition: A qubit is a quantum bit that can be in a state of |0⟩, |1⟩, or both (superposition).  
Superposition Example: A qubit can represent both 0 and 1 simultaneously, enabling parallel processing.  
Measurement: When measured, a qubit collapses to a definite state (0 or 1).

2.2 Entanglement  
Entangled Qubits: Qubits can be linked such that the state of one instantly influences the other, even at a distance.  
Example: In a Bell pair, measuring one qubit determines the state of the other.

2.3 Quantum Gates  
Hadamard Gate (H): Creates superposition.  
CNOT Gate: Entangles qubits.  
Pauli Gates: Flip qubit states (X, Y, Z).

2.4 Quantum Algorithms  
Shor’s Algorithm: Factorizes large numbers exponentially faster than classical methods, threatening RSA encryption.  
Grover’s Algorithm: Searches unsorted databases quadratically faster than classical algorithms.  
Quantum Fourier Transform (QFT): Enables efficient analysis of periodic functions, critical for algorithms like Shor’s.

3. **Quantum Gates and Circuits**
Quantum circuits are sequences of quantum gates that perform computations. Key components include:
- Initialization: Qubits are set to |0⟩ or |1⟩.
- Gates: Operations like Hadamard, CNOT, and Pauli gates manipulate qubits.
- Measurement: Final results are obtained by measuring qubits.

Example: A quantum circuit for a Quantum Full Adder performs bitwise addition using quantum gates.

4. **Quantum Algorithms**
4.1 Shor’s Algorithm  
Purpose: Factorizes large integers (e.g., RSA encryption).  
Mechanics: Uses QFT and quantum phase estimation to solve the factorization problem.

4.2 Grover’s Algorithm  
Purpose: Searches unsorted databases quadratically faster than classical algorithms.  
Application: Used in quantum search and optimization problems.

4.3 Other Algorithms  
Deutsch-Jozsa Algorithm: Determines if a function is constant or balanced.  
Simon’s Algorithm: Solves the hidden subgroup problem.  
Quantum Walks: Improve problem-solving by leveraging entanglement and parallelism.

5. **Quantum Hardware and Error Correction**
5.1 Quantum Hardware  
Qubit Types: Superconducting qubits (IBM, Google), trapped ions (IonQ), and photons (Quantum Science Center).  
Challenges: Decoherence (loss of quantum state), error rates, and scalability.

5.2 Quantum Error Correction (QEC)  
Purpose: Mitigate errors caused by decoherence.  
Techniques:  
- Surface Code: Encodes a logical qubit across multiple physical qubits.  
- Topological Qubits: Use error-correcting codes to protect qubits.  
Example: Q-CTRL’s Quantum Error Correction Stack and Neutral Atoms’ Aquila system address scalability challenges.

6. **Applications in Cryptography, Optimization, and Drug Discovery**
6.1 Cryptography  
Quantum Threats: Shor’s algorithm threatens RSA and ECC encryption.  
Quantum Solutions: Post-quantum cryptography (e.g., lattice-based encryption) and quantum key distribution (QKD).

6.2 Optimization  
Quantum Speedup: Solving complex problems like the Traveling Salesman Problem (TSP) exponentially faster.  
Example: QAOA (Quantum Approximate Optimization Algorithm) for logistics and finance.

6.3 Drug Discovery  
Quantum Simulations: Simulate molecular interactions to design new drugs.  
Example: IBM’s quantum chemistry calculations for new materials to capture carbon more efficiently.

7. **Practical Examples and Implementation**
7.1 Qiskit and Cirq  
Qiskit: IBM’s Python framework for simulating and executing quantum algorithms.  
Cirq: Google’s framework for simulating NISQ (Noisy Intermediate-Scale Quantum) computers.

Example:  
- Grover’s Algorithm: Implemented in Qiskit using a custom circuit with Hadamard gates and oracle operations.  
- Quantum Fourier Transform: Used in Qiskit for simulating quantum systems.

7.2 Real-World Applications  
- Healthcare: Quantum simulations for protein folding and drug discovery.  
- Finance: Quantum algorithms for portfolio optimization and risk assessment.  
- Energy: Quantum simulations for renewable energy and power grid optimization.

8. **Educational Resources and Learning Pathways**
8.1 Learning Platforms  
- Coursera:  
  - Quantum Computing For Everyone (KAIST)  
  - Python Programming for Quantum Computing  
- edX:  
  - Quantum Mechanics for Engineers  
  - Quantum AI  
- D-Wave Training:  
  - Quantum Programming Core Course (1-week self-paced)

8.2 Tools and Simulators  
- Qiskit: Simulate quantum circuits on IBM’s quantum hardware.  
- Cirq: Simulate NISQ computers.  
- Aer: Qiskit’s simulator for high-performance quantum computations.

8.3 Community and Collaboration  
- Q-CTRL: Quantum error correction frameworks.  
- Neutral Atoms: 256-qubit Aquila system and Bloqade software.  
- Industry Partnerships: Collaborations between academia and companies (e.g., Riverlane, Q-CTRL).

9. **Conclusion and Future Outlook**
Quantum computing represents a paradigm shift, leveraging quantum mechanics to solve problems exponentially faster than classical computers. Key applications span cryptography, optimization, drug discovery, and materials science, with real-world examples like IBM’s quantum simulations and ExxonMobil’s energy innovations.

**Challenges:**
- Decoherence: Requires extreme control environments (e.g., cryogenic systems).
- Error Correction: Critical for fault-tolerant quantum computing.

**Future Prospects:**
- Quantum Supremacy: Solving problems intractable for classical systems.
- Commercialization: Industry investment (e.g., $1.3 trillion by 2035) will drive advancements.

**Educational Value:**
- Skills: Mastery of quantum mechanics, programming (Python, Qiskit), and optimization techniques.
- Career Opportunities: Quantum software development, hardware engineering, and research.

**Final Summary**
Quantum computing is a transformative field with immense potential to revolutionize industries. By understanding fundamental concepts, algorithms, and practical implementations, students and professionals can harness quantum technologies to solve complex problems, from cryptography to drug discovery. As quantum hardware advances, the integration of quantum principles into real-world applications will drive innovation in science, engineering, and business.
"""

if submit:
    if not api_key:
        st.error("Please provide your Together API key.")
        st.stop()

    st.info("Generating notes... This may take a minute.")
    client = Together(api_key=api_key)

    user_prompt = (
        f"Create {depth} educational notes on the topic: '{topic}'.\n"
        f"Target audience: {audience}.\n"
        f"{'Include examples.' if include_examples else 'No need for examples.'}\n"
        "Structure the notes with clear sections, explanations, and educational value."
    )

    try:
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
            messages=[
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=2048,
            temperature=0.7,
            top_p=0.8
        )
        notes = response.choices[0].message.content
        st.success("Notes generated successfully!")
        st.markdown(f"### Notes on: {topic}")
        st.markdown(notes)
    except Exception as e:
        st.error(f"Error: {e}")

if example:
    st.info("Showing example output for Quantum Computing.")
    st.markdown(EXAMPLE_NOTES)
