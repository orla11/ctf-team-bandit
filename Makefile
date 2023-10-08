.PHONY: format
format:
	black ./ctf_team_bandit/

.PHONY: start-ctf
start-ctf:
	poetry run python3 ctf_team_bandit/ctf_team_bandit.py