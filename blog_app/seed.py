import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from blog_app import models, database
from blog_app.database import SessionLocal
from blog_app.logging_config import get_logger

logger = get_logger(__name__)

def seed_db():
    db = SessionLocal()
    
    # Check if we already have posts
    if db.query(models.Post).count() > 0:
        logger.info("Database already seeded.")
        db.close()
        return

    posts = [
        # Lifestyle - Gym Workouts
        models.Post(
            title="The Art of the Morning Lift",
            category="Lifestyle",
            summary="Why sunrise sessions are the ultimate discipline for the modern athlete.",
            content="""There is a particular kind of silence that only exists at 5:30 AM in a weight room. It's a heavy, expectant quiet, broken only by the rhythmic clang of plates and the distant hum of the city waking up.

Starting your day with a focused workout isn't just about physical hypertrophy; it's a psychological victory. When you've already conquered a heavy squat set before most people have hit snooze, you move through the rest of your day with an unshakeable confidence.

Key Workout Routine:
1. Warm-up: 10 mins dynamic stretching.
2. Compound Movement: 5x5 Barbell Squats or Deadlifts.
3. Accessory: 3x12 Weighted Lunges.
4. Core: 3 sets of Plank (60s).

Focus on the mind-muscle connection. It's not about the weight on the bar, but the intention behind every rep.""",
            featured_image="https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=2000&auto=format&fit=crop"
        ),
        models.Post(
            title="Functional Strength: Beyond the Mirror",
            category="Lifestyle",
            summary="Moving from aesthetic goals to performance-based longevity.",
            content="""For too long, the fitness industry has been obsessed with how muscles look rather than how they function. True strength is the ability to move through the world with ease and resilience.

Incorporating kettlebell swings, pull-ups, and odd-object carries into your routine builds a type of 'farm strength' that translates directly to real-life activities. Whether it's carrying groceries, hiking a steep trail, or simply maintaining perfect posture during a long flight, functional training is the foundation of a high-quality life.

Don't just train for the beach; train for the next four decades of your life.""",
            featured_image="https://images.unsplash.com/photo-1517836357463-d25dfeac3438?q=80&w=2000&auto=format&fit=crop"
        ),
        
        # Journal - Diets & Supplements
        models.Post(
            title="The Clean Slate: A Guide to Whole Foods",
            category="Journal",
            summary="Simplifying your nutrition in an age of processed complexity.",
            content="""The most revolutionary thing you can do for your health today is to return to the basics. In a world of 'superfood' marketing and complex diet hacks, the humble vegetable and the high-quality protein source remain the undisputed kings of nutrition.

A 'Clean Slate' approach focuses on:
- Single-ingredient foods.
- Seasonal produce from local sources.
- Adequate hydration (3L+ daily).
- Minimal added sugars and industrial seed oils.

When you fuel your body with what it was designed to consume, the brain fog lifts, energy levels stabilize, and the body naturally finds its optimal weight. It's not a diet; it's a biological homecoming.""",
            featured_image="https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=2000&auto=format&fit=crop"
        ),
        models.Post(
            title="Supplements: The 5% Edge",
            category="Journal",
            summary="Cutting through the noise to find what actually works for performance and recovery.",
            content="""Let's be clear: you cannot out-supplement a poor diet or lack of sleep. However, once your foundation is solid, strategic supplementation can provide the '5% edge' that elevates your performance from good to elite.

The Essentials for the Modern Individual:
1. Vitamin D3 + K2: Crucial for bone health and immune function, especially for those in northern climates.
2. Magnesium Bisglycinate: The ultimate recovery mineral. Improves sleep quality and reduces muscle cramps.
3. Omega-3 Fish Oil: For brain health and reducing systemic inflammation.
4. Creatine Monohydrate: The most researched performance supplement in history. Safe, effective, and essential for cognitive and physical output.

Always consult with a professional, but keep your stack simple and science-backed.""",
            featured_image="https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?q=80&w=2000&auto=format&fit=crop"
        ),
    ]

    for post in posts:
        db.add(post)
    
    db.commit()
    logger.info("Database successfully seeded with lifestyle and journal content.")
    db.close()

if __name__ == "__main__":
    seed_db()
