# Evaluation of Candidates for GitHub and GitLab Integration

## Candidates

- **[GitHub MCP by GitHub](https://github.com/github/github-mcp-server)**
  - Version: 0.33.0
  - What: official MCP server by GitHub to read and write a repository, including issues and pull requests

- **[GitLab MCP by GitLab](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server_tools/)**
  - Version of GitLab: 18.10.0-ee
  - What: official MCP server by GitLab to read and write a repository, including issues and merge requests

- **[GitLab MCP by zereight](https://github.com/zereight/gitlab-mcp)**
  - Version: 2.1.1
  - What: third-party MCP server to read and write a repository, including issues and merge requests

## Requirements Analysis

### Work With Up-to-Date Information

- **GitHub MCP by GitHub**
  - Rating: ++
  - Strengths:
    - Tool provides various features to read and write GitHub data, including private repositories.
    - Tool provides read-only mode.
  - Weaknesses:
    - None

- **GitLab MCP by GitLab**
  - Rating: +
  - Strengths:
    - Tool provides various features to read and write GitLab data, including private repositories.
    - User can configure tool with restricted read-only toolset
  - Weaknesses:
    - None

- **GitLab MCP by zereight**
  - Rating: ++
  - Strengths:
    - Tool provides various features to read and write GitLab data, including private repositories.
    - Tool provides read-only mode.
  - Weaknesses:
    - None

### Latency Optimization

- **GitHub MCP by GitHub**
  - Rating: +
  - Strengths:
    - Read-only mode with smaller toolset improves latency
  - Weaknesses:
    - Overhead due to MCP layer

- **GitLab MCP by GitLab**
  - Rating: +
  - Strengths:
    - Manually configured read-only toolset improves latency
  - Weaknesses:
    - Overhead due to MCP layer

- **GitLab MCP by zereight**
  - Rating: +
  - Strengths:
    - Read-only mode with smaller toolset improves latency
  - Weaknesses:
    - Overhead due to MCP layer

### Not Share User Data

- **GitHub MCP by GitHub**
  - Rating: --
  - Strengths:
    - None
  - Weaknesses:
    - Authentication via personal access token or OAuth. Anonymous access not possible.

- **GitLab MCP by GitLab**
  - Rating: --
  - Strengths:
    - None
  - Weaknesses:
    - Authentication via OAuth. Anonymous access not possible.

- **GitLab MCP by zereight**
  - Rating: --
  - Strengths:
    - None
  - Weaknesses:
    - Authentication via personal access token or OAuth. Anonymous access not possible.

### Implementation Effort

- **GitHub MCP by GitHub**
  - Rating: +
  - Strengths:
    - Tool enables authentication via a personal access token, which works well for the desktop app of OpenCode and Kilo Code, in comparison to OAuth authentication.
  - Weaknesses:
    - Cumbersome process to set up a Docker container
    - User must store personal access token in a separate file. Environment variable does not seem to be possible.

- **GitLab MCP by GitLab**
  - Rating: --
  - Strengths:
    - Not relevant
  - Weaknesses:
    - Access to the European XFEL GitLab server is not possible because the GitLab server neither has [GitLab Duo nor experimental tools enabled](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server_troubleshooting/#404-not-found-when-starting-the-gitlab-mcp-server). Installation requires actions by server admins.

- **GitLab MCP by zereight**
  - Rating: ++
  - Strengths:
    - Tool can access the European XFEL GitLab server because it simply wraps the GitLab API with an MCP layer. It does not require additional server features, such as GitLab Duo.
    - Tool enables authentication via a personal access token, which works well for the desktop app of OpenCode and Kilo Code, in comparison to OAuth authentication.
    - User can simply set up a Docker container.
  - Weaknesses:
    - None

### Component Replacement Effort

- **GitHub MCP by GitHub**
  - Rating: ++
  - Strengths:
    - User could quickly switch to another GitHub MCP server.
  - Weaknesses:
    - None

- **GitLab MCP by GitLab**
  - Rating: ++
  - Strengths:
    - User could quickly switch to another GitLab MCP server.
  - Weaknesses:
    - None

- **GitLab MCP by zereight**
  - Rating: ++
  - Strengths:
    - User could quickly switch to another GitLab MCP server.
  - Weaknesses:
    - None
