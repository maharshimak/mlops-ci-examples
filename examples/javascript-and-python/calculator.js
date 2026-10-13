// calculator.js — run with: node calculator.js

const readline = require("readline");

// ---------- Tokenizer ----------
function tokenize(expr) {
  const tokens = [];
  let i = 0;

  while (i < expr.length) {
    const ch = expr[i];

    if (/\s/.test(ch)) { i++; continue; }

    if (/[0-9.]/.test(ch)) {
      let num = "";
      while (i < expr.length && /[0-9.]/.test(expr[i])) num += expr[i++];
      if ((num.match(/\./g) || []).length > 1) throw new Error(`Invalid number: ${num}`);
      const value = Number(num);
      if (!Number.isFinite(value)) throw new Error("Invalid number");
      tokens.push({ type: "num", value });
      continue;
    }

    if ("+-*/%^()".includes(ch)) {
      tokens.push({ type: "op", value: ch });
      i++;
      continue;
    }

    throw new Error(`Unexpected character: '${ch}'`);
  }
  return tokens;
}

// ---------- Parser (recursive descent) ----------
// expr   := term (('+' | '-') term)*
// term   := factor (('*' | '/' | '%') factor)*
// factor := unary ('^' factor)?        (right-associative)
// unary  := ('-' | '+') unary | primary
// primary:= number | '(' expr ')'
function evaluate(expr) {
  if (typeof expr !== "string" || expr.length > 4096) throw new Error("Expression must be a string of at most 4096 characters");
  const tokens = tokenize(expr);
  let pos = 0;

  const peek = () => tokens[pos];
  const next = () => tokens[pos++];
  const isOp = (v) => peek() && peek().type === "op" && peek().value === v;

  function parseExpr() {
    let left = parseTerm();
    while (isOp("+") || isOp("-")) {
      const op = next().value;
      const right = parseTerm();
      left = op === "+" ? left + right : left - right;
    }
    return left;
  }

  function parseTerm() {
    let left = parseFactor();
    while (isOp("*") || isOp("/") || isOp("%")) {
      const op = next().value;
      const right = parseFactor();
      if ((op === "/" || op === "%") && right === 0) throw new Error("Division by zero");
      if (op === "*") left *= right;
      else if (op === "/") left /= right;
      else left %= right;
    }
    return left;
  }

  function parseFactor() {
    const base = parseUnary();
    if (isOp("^")) {
      next();
      return Math.pow(base, parseFactor());
    }
    return base;
  }

  function parseUnary() {
    if (isOp("-")) { next(); return -parseUnary(); }
    if (isOp("+")) { next(); return parseUnary(); }
    return parsePrimary();
  }

  function parsePrimary() {
    const tok = next();
    if (!tok) throw new Error("Unexpected end of expression");
    if (tok.type === "num") return tok.value;
    if (tok.value === "(") {
      const val = parseExpr();
      if (!isOp(")")) throw new Error("Missing closing parenthesis");
      next();
      return val;
    }
    throw new Error(`Unexpected token: '${tok.value}'`);
  }

  const result = parseExpr();
  if (pos < tokens.length) throw new Error(`Unexpected token: '${peek().value}'`);
  return result;
}

// ---------- Interactive CLI ----------
if (require.main === module) {
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

  console.log("JS Calculator — type an expression (e.g. 2 + 3 * (4 - 1) ^ 2), or 'exit' to quit.");
  rl.setPrompt("> ");
  rl.prompt();

  rl.on("line", (line) => {
    const input = line.trim();
    if (input === "exit" || input === "quit") return rl.close();
    if (input) {
      try {
        const result = evaluate(input);
        // Round off floating-point noise like 0.1 + 0.2 = 0.30000000000000004
        console.log("=", Number(result.toFixed(10)));
      } catch (err) {
        console.log("Error:", err.message);
      }
    }
    rl.prompt();
  });

  rl.on("close", () => console.log("Bye!"));
}

module.exports = { evaluate };
