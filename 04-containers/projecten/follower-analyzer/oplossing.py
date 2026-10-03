"""follower-analyzer — vergelijk je volgers op twee platformen."""

TIKTOK = ["alice", "bob", "carol", "dave", "alice"]
INSTAGRAM = ["carol", "dave", "erin", "frank"]

tiktok = set(TIKTOK)
instagram = set(INSTAGRAM)

gedeeld = tiktok & instagram
uniek = tiktok ^ instagram
totaal = tiktok | instagram

print("Volgers op beide platformen:", sorted(gedeeld))
print("Volgers op slechts één platform:", sorted(uniek))
print(f"Totaal unieke volgers: {len(totaal)}")
