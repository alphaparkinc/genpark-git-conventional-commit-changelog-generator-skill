import sys
import json
from client import ConventionalCommitGenerator

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-git-conventional-commit-changelog-generator-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "generate_conventional_commit",
                        "description": "Analyze code diff and synthesize conventional commit message",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "diff_text": {"type": "string", "description": "Git diff patch text"}
                            },
                            "required": ["diff_text"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        
        if tool_name == "generate_conventional_commit":
            d = args.get("diff_text", "")
            msg = ConventionalCommitGenerator.synthesize_commit(d)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": msg}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
