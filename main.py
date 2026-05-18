import sys

from core.comparison_engine import analyze_debate
from cli.args import get_args
from utils.logger import get_logger

logger = get_logger()

debate = """
Speaker A: You are the dumbest person alive
Speaker B: That's an ad hominem attack, not a real argument

Speaker A: Fine, but everyone agrees with me, so I must be right
Speaker B: Popularity doesn't make something true

Speaker A: Think about the poor children suffering if we don't act
Speaker B: You're appealing to emotion instead of giving evidence

Speaker A: So you're saying we should just ignore the problem completely?
Speaker B: No, that's not what I said at all

Speaker A: Either we accept this solution or everything will fail
Speaker B: That's a false dilemma, there are other options

Speaker A: If we allow this small change, society will collapse
Speaker B: That's a slippery slope argument

Speaker A: All politicians are corrupt anyway
Speaker B: That's a hasty generalization

Speaker A: Why are we even talking about this when there are bigger issues?
Speaker B: That's a red herring, stay on topic

Speaker A: This policy is wrong because it's bad
Speaker B: That's circular reasoning

Speaker A: You're too inexperienced to understand this topic
Speaker B: Attacking my experience doesn't invalidate my argument

Speaker A: If you disagree, you're basically against progress
Speaker B: That's another false dilemma

Speaker A: This is obviously true because everyone knows it
Speaker B: That's not evidence, just repetition

Speaker A: You always twist my words
Speaker B: Point out exactly where instead of making vague claims

Speaker A: This will destroy our future generations
Speaker B: Again, that's emotional exaggeration without proof
"""
try:
    result = analyze_debate(debate)
    logger.info("Debate analysis completed successfully")
    print(result)

except Exception as e:
    logger.error(f"Pipeline failed: {str(e)}")
