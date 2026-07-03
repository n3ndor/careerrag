// Embedding edge function: wraps Supabase's built-in gte-small model (384 dims).
// Called by BOTH the Python indexer (index time) and the chat API route
// (query time) so one model is used everywhere.
//
// POST { "input": "text" }            -> { "embeddings": [[...384 floats]] }
// POST { "input": ["a", "b", ...] }   -> { "embeddings": [[...], [...]] }

const session = new Supabase.ai.Session("gte-small");

const MAX_BATCH = 32;
const MAX_CHARS = 8000;

Deno.serve(async (req) => {
  if (req.method !== "POST") {
    return json({ error: "POST only" }, 405);
  }

  let input: unknown;
  try {
    ({ input } = await req.json());
  } catch {
    return json({ error: "invalid JSON body" }, 400);
  }

  const texts = Array.isArray(input) ? input : [input];
  if (
    texts.length === 0 ||
    texts.length > MAX_BATCH ||
    texts.some((t) => typeof t !== "string" || t.length === 0 || t.length > MAX_CHARS)
  ) {
    return json(
      { error: `input must be 1-${MAX_BATCH} non-empty strings of <= ${MAX_CHARS} chars` },
      400,
    );
  }

  const embeddings: number[][] = [];
  for (const text of texts as string[]) {
    const embedding = await session.run(text, { mean_pool: true, normalize: true });
    embeddings.push(embedding as number[]);
  }

  return json({ embeddings });
});

function json(body: unknown, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}
