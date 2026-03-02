from typing import Dict, Any, List

I18N_DATA = {
    "en": {
        "ENERGY_TRAITS": {
            "Wood": {
                "name": "Unstoppable Growth (Wood) 🌲",
                "desc_intro": [
                    "You literally radiate that 'Main Character' giant tree energy. In K-Saju, Wood is all about vitality, curiosity, and leveling up non-stop."
                ],
                "desc_core": {
                    "E": [
                        "You carry everybody forward in the best way. Outgoing and super focused on growing your squad."
                    ],
                    "I": [
                        "Silent but deadly. You level up without telling anyone and drop the final results to shock everyone."
                    ],
                    "default": [
                        "You're a try-hard in the best way possible. Always ready for side quests and fearless. You can be a bit nosy, but deep down you just want your whole squad to win.\n\nYou're flexible, but cross your bottom line and you stand firm like a GOAT. That stubborn streak is your ultimate rizz."
                    ]
                },
                "desc_career": [
                    "[CEO Mindset]\nYou belong in spaces where you can hustle and create. Startup founder, editor, content creator—you literally serve looks and ideas from scratch. Desk jobs? Big yikes. You need that dopamine hit of making moves!"
                ],
                "desc_advice": [
                    "[Glow-up Guide]\nRed flag: Starting 10 things and finishing none. You need to focus and tunnel-vision on one goal, and you will absolutely crush it."
                ]
            },
            "Fire": {
                "name": "Blazing Flame (Fire) 🔥",
                "desc_intro": [
                    "Your soul gives off major 'Sun' energy. You're a walking torch! Fire means god-tier passion, expansion, and zero filter."
                ],
                "desc_core": {
                    "E": [
                        "Literally the life of the party. You fill up the room with loud, vibrant energy."
                    ],
                    "I": [
                        "A loyal, warm hearth only to those you truly appreciate. You save your fire for the right ones."
                    ],
                    "default": [
                        "You steal the show effortlessly, just being there is serving. Your battery is always at 100%, and your over-the-top reactions make you the ultimate hype-person for your besties. You're 100% transparent, zero grudges even after a massive drama.\n\nFire values respect. You're the sweetest to those who pass the vibe check, but cross the line? Demon mode activated."
                    ]
                },
                "desc_career": [
                    "[CEO Mindset]\nYou were born for the stage. Influencer, marketing, PR—you leave no crumbs. Sitting at a desk will kill your vibe instantly."
                ],
                "desc_advice": [
                    "[Glow-up Guide]\nWith your crazy mood swings, you sometimes go 0 to 100 real quick. Breathing for 3 seconds before roasting someone in the group chat is your ultimate life hack."
                ]
            },
            "Earth": {
                "name": "Solid Ground (Earth) ⛰️",
                "desc_intro": [
                    "Your soul is like the 'Vast Earth' that embraces everything. Earth is about mediating, being trustworthy, and having an unshakable vibe."
                ],
                "desc_core": {
                    "E": [
                        "You keep everyone together. Friendly, sociable, and the best person at giving advice."
                    ],
                    "I": [
                        "Total tsundere. You secretly care for your close ones with brutal loyalty, even if you don't open up easily."
                    ],
                    "default": [
                        "Zero ghosting. You have a titanium mindset and act as the power bank for your mutuals. You're the mediator who squashes squad beef. Total tsundere, you secretly care for everyone and are hyper-loyal.\n\nBut plot twist: being quiet doesn't mean you're a pushover. When Earth gets mad, it's an earthquake. You naturally spit heavy facts when the time comes."
                    ]
                },
                "desc_career": [
                    "[CEO Mindset]\nYou prefer secured bags over impulsive risks. HR, finance, education—you're the GOAT at building teams and fixing broken stuff."
                ],
                "desc_advice": [
                    "[Glow-up Guide]\nPutting everyone else first will give you insane burnout. Starting your 'villain era' and prioritizing YOURSELF is the ultimate green flag you need right now."
                ]
            },
            "Metal": {
                "name": "Sharp Blade (Metal) ⚔️",
                "desc_intro": [
                    "Your soul screams 'Flawless Jewel' and 'Sharp Blade'. Metal is the poster child for perfectionism and cold hard logic, giving major boss energy."
                ],
                "desc_core": {
                    "E": [
                        "Rational and lethal. You lead with firmness, ignore excuses, and always get the project done."
                    ],
                    "I": [
                        "You observe coldly and only speak when 100% necessary. You have life standards that are unreachable for many."
                    ],
                    "default": [
                        "A hard 'T' with zero patience for messiness. You ghost emotional drama and operate like a cold CEO. Once you lock onto a goal, your tunnel vision is insane.\n\nThough you seem like an ice king/queen, your loyalty for your inner circle goes hard. If a friend gets attacked, you activate bodyguard mode."
                    ]
                },
                "desc_career": [
                    "[CEO Mindset]\nYou shine with numbers and hard code. Tech, law, med. You're a workaholic who lets the 'receipts' (results) do the talking."
                ],
                "desc_advice": [
                    "[Glow-up Guide]\nYour sky-high standards can trap you in toxic perfectionism. Chilling out and showing your messy side will make people ship you even more."
                ]
            },
            "Water": {
                "name": "Free Flowing (Water) 🌊",
                "desc_intro": [
                    "Your soul flows with the deep, mysterious vibe of the 'Ocean'. Water means 200 IQ wisdom, total adaptability, and mental depth."
                ],
                "desc_core": {
                    "E": [
                        "You adapt in every social group. You can chat with anyone and pull info effortlessly."
                    ],
                    "I": [
                        "Misunderstood genius. You hold immense truths in silence and occasionally shatter everything with a deep realization."
                    ],
                    "default": [
                        "You're the ultimate shapeshifter. You pass every vibe check and fit any aesthetic. Your thoughts are Mariana-Trench deep; you have an intuition that gives 'nerd but aesthetic' vibes.\n\nYou might look soft, but you have beast-like endurance. Yet, since you keep things to yourself, people might think you're living in your own 'delulu' world."
                    ]
                },
                "desc_career": [
                    "[CEO Mindset]\nRules? We don't know her. Digital nomad, researcher, creator—you need max flexibility to let your inner genius cook."
                ],
                "desc_advice": [
                    "[Glow-up Guide]\nOverthinking is your biggest opp, sinking you into your sad-boy/sad-girl era. Turn off the brain and go 'touch grass' literally; that's how you win the game."
                ]
            }
        },
        "MONTH_FORTUNES": {
            "1": {
                "theme": "Vibe of New Beginnings, '{dominant}' Energy 🌱",
                "signal": "Best month to set goals with {idol}. Synergy will explode!",
                "guide": "God-mode activated! Start with 10min of reading or exercise. 💰 Wealth is rising!"
            },
            "2": {
                "theme": "Intellectual Achievement & Reflection 📚",
                "signal": "You'll be inspired by {idol}'s intellectual side. Deep talks are a go.",
                "guide": "Invest in learning. New certifications or study will be a huge asset."
            },
            "3": {
                "theme": "Spring Vitality & Social Expansion 🌸",
                "signal": "Perfect timing for outdoor activities or events with {idol}.",
                "guide": "New connections are coming. Be active in social circles. 💓 Love vibes UP!"
            },
            "4": {
                "theme": "Passionate Energy & Growth Acceleration 🔥",
                "signal": "{idol}'s passion will motivate you. Take the challenge together!",
                "guide": "Start what you've delayed. Execution now decides your final results."
            },
            "5": {
                "theme": "Building Stability & Inner Peace ⛰️",
                "signal": "Great month for relaxing and building a deep bond with {idol}.",
                "guide": "Clean your space. A clear environment means a clear flow of luck."
            },
            "6": {
                "theme": "Communication Explosion & Creative Ideas 💡",
                "signal": "Expect fun news or a surprise interaction with {idol} this month.",
                "guide": "Record your ideas. A small thought could lead to a massive project."
            },
            "7": {
                "theme": "Intense Emotions & Intuition Peak 🌊",
                "signal": "Your destiny frequency with {idol} gets stronger. Pure stan mood.",
                "guide": "Trust your gut. The answer is already inside your soul's compass."
            },
            "8": {
                "theme": "Harvest Prelude & Preparation for Abundance ⚔️",
                "signal": "Celebrate {idol}'s career wins and share some positive energy.",
                "guide": "Focus on health. Regular habits will charge your base spirit level."
            },
            "9": {
                "theme": "Careful Judgment & Re-setting Goals 🎯",
                "signal": "Check your end-of-year plans with {idol} and sync your vibes.",
                "guide": "Manage your bag. Cut useless costs to find bigger opportunities."
            },
            "10": {
                "theme": "Deep Understanding & Spiritual Growth 🔮",
                "signal": "You will understand {idol}'s hidden message or heart today.",
                "guide": "Write a journal or meditate. Luck opens when you listen to your inner self."
            },
            "11": {
                "theme": "Wave of Change & Flexible Tactics 🌊",
                "signal": "Cheer on {idol}'s new activities and exchange cosmic energy.",
                "guide": "Go with the flow. Growth comes when you're not afraid of change."
            },
            "12": {
                "theme": "Completion & Rest for New Dreams ❄️",
                "signal": "A warm month to wrap up the year with a full heart for {idol}.",
                "guide": "Treatment time! Rewarding yourself keeps your energy at its peak."
            }
        },
        "LIFETIME_STAGES": {
            "Wood": {
                "youth": "[Early: Spring Sprout] A period of high curiosity and a strong desire to learn. In your 10s and 20s, you will blossom with help from others.",
                "young_adult": "[Youth: Lush Tree] Establishing your own domain as you enter society. In your 30s and 40s, you will reach your career peak with strong drive.",
                "middle_age": "[Midlife: Strong Roots] Accumulated experience bears fruit, providing a stable foundation. In your 50s and 60s, you will shine as a leader or mentor.",
                "senior": "[Late: Rich Forest] Respected by those around you, living a peaceful life. After your 70s, mental leisure and honor will follow."
            },
            "Fire": {
                "youth": "[Early: Burning Flame] A passionate and creative period. In your 10s and 20s, you will make your presence known through spotlighted activities.",
                "young_adult": "[Youth: Midday Sun] Your most active period with explosive results. In your 30s and 40s, you will lead change and create new trends.",
                "middle_age": "[Midlife: Gentle Lamp] Controlling inner passion to wisely light up your surroundings. In your 50s and 60s, you will lead as the center of an organization.",
                "senior": "[Late: Beautiful Sunset] Living as a wise advisor with rich experiences. After your 70s, you will find happiness in culture, art, or spiritual rest."
            },
            "Earth": {
                "youth": "[Early: Earth's Nutrient] Building basics and gaining trust. In your 10s and 20s, silent efforts will manifest as achievements or certifications.",
                "young_adult": "[Youth: Fertile Soil] Cooperating with many and building wealth. In your 30s and 40s, you will focus on stable assets and building a family.",
                "middle_age": "[Midlife: Great Mountain] Leading large organizations or businesses with unwavering conviction. In your 50s and 60s, you will gain fame as a mediator.",
                "senior": "[Late: Vast Land] Feeling deep reward through giving and sharing. After your 70s, you will enjoy a peaceful old age with prosperous descendants."
            },
            "Metal": {
                "youth": "[Early: Sharp Blade] Developing clear goals and decisiveness. In your 10s and 20s, you will stand out by gaining an upper hand in competition.",
                "young_adult": "[Youth: Gem's Radiance] Proving your value with sophisticated sense and expertise. In your 30s and 40s, you will gather great wealth based on clear standards.",
                "middle_age": "[Midlife: Strong Steel] Having the experience and authority to accomplish anything. In your 50s and 60s, you will exert great power at the peak of strategy.",
                "senior": "[Late: Noble Gold] Maintaining a dignified life and focusing on inner completion. After your 70s, you will live comfortably summarizing your life's value."
            },
            "Water": {
                "youth": "[Early: Clear Spring] Wise and clever, living up to high expectations. In your 10s and 20s, you will master various fields with flexible thinking.",
                "young_adult": "[Youth: Winding River] Gaining rich experience in the wide world. In your 30s and 40s, you will catch unexpected opportunities through movement or change.",
                "middle_age": "[Midlife: Deep Lake] Becoming a spiritual leader based on vast knowledge and insight. In your 50s and 60s, you will expand your influence quietly.",
                "senior": "[Late: Endless Sea] Finding peace with a broad heart like a sea that embraces all. After your 70s, you will find joy in travel or academic pursuit."
            }
        },

        "LOVE_STYLES": [
            "Looks quiet, but once they want you, they have massive fox energy and will slide in smooth. They secretly memorize all your lore.",
            "Golden retriever energy! They give you top-tier loyalty. You drop a text and they reply before the notification even hits.",
            "Total tsundere. Cold and unbothered to the world, but a complete softie for you. The gap-moe is their deadliest weapon.",
            "The ultimate green flag. They love daily check-ins and late-night aesthetic calls over loud, expensive surprises.",
            "Feral cat vibes. They fiercely protect their alone time. Respect their space and hustle, and they'll naturally obsess over you."
        ],
        "ELEMENT_SYNERGY": {
            "생": "[Ultimate Duo] Y'all basically complete each other's sentences. You elevate their ideas to the moon. 200% synergy, the ultimate endgame pair.",
            "극": "[Spicy Dynamic] Opposite aesthetics but fatal attraction. Enemies to lovers trope. You bicker, but the chemistry is electric and forces massive growth.",
            "비화": "[Mirror Soulmates] You pass the same vibe check without speaking. Same humor, same unhinged thoughts. The ultimate besties for life."
        },
        "TIPS": [
            "Stop playing games! Trying to make them jealous is an instant ick. Direct, unfiltered honesty is your only cheat code.",
            "Skip the boring coffee dates. Hit them with a high-dopamine, unhinged surprise adventure.",
            "Hype them up 24/7! Endless glazer-level compliments will literally melt their defenses.",
            "Being clingy is a massive red flag. Show off your own independent boss energy—that's what makes them go crazy.",
            "Instead of loud flexes, casually gift them that niche thing they tweeted about 3 weeks ago. Taking notes is mandatory!",
            "Mystery is your best friend. Don't reveal all your lore at once; keep them guessing for the next chapter.",
            "Visuals matter! Send them an aesthetic 'vibe check' photo of your day to keep the connection alive.",
            "Acts of service go a long way. Quietly handle that one chore they hate—it's a major green flag.",
            "Share your vulnerability. Showing the 'real' you behind the filter creates a deep, unbreakable bond.",
            "Be their biggest defender. Standing up for them in the group chat is the ultimate loyalty test.",
            "Create a 'just for us' tradition. Even a small weekly ritual makes the relationship feel elite.",
            "Physical touch (when the vibe is right) is a game changer. A subtle, well-timed gesture speaks volumes.",
            "Respect their 'Do Not Disturb' mode. Giving space is as important as giving attention.",
            "Level up together. Start a shared hobby or project to build a power-duo dynamic.",
            "Keep the banter sharp! A little playful roasting is the secret sauce to keeping the sparks flying."
        ],
        "MISSION_FRAGMENTS": {
            "labels": [
                "God-tier Taste Sync 📸", "Soul Connection Deep-Dive 💬", "Dopamine Healing Arc 🎡",
                "Cosmic Aesthetic Merge ✨", "Main Character Energy Sync 🌟", "Secret Lore UNLOCKED 🔑"
            ],
            "reasons": [
                "Based on the unique {u_el} vs {i_el} energy magnetic field.",
                "Analyzing the {u_mbti} & {i_mbti} psychological communication gap.",
                "Synchronizing the destined soul frequency between you two.",
                "Optimizing the elemental flow for a perfect support-carry dynamic.",
                "Resolving the hidden friction in your collective cosmic charts.",
                "Amplifying the latent synergy for an unstoppable power-duo era."
            ]
        },
        "UI_STRINGS": {
            "profile": "👤 Profile",
            "mbti_unrevealed": "Gatekept / Unknown",
            "signature": "🔮 [Your Core Aesthetic]",
            "potential": "💫 [Hidden Lore & Power]",
            "stage": "💼 [Where You Slay the Hardest]",
            "guide": "🚀 [2026 Glow-Up Cheat Sheet]",
            "idol_mbti_fallback": "Unknown (Vibe matched via '{trait_name}')",
            "idol_mbti_fallback_random": "Unknown (Destiny matched by fate)",
            "pure_saju_label": "🌟 Deep Soul Resonance (MBTI Excluded)",
            "mbti": "MBTI",
            "selectType": "Select Type",
            "female": "Female",
            "male": "Male",
            "nonbinary": "Non-binary",
            "friendInfoTitle": "FRIEND / PARTNER INFO",
            "friendBirthLabel": "Friend Birth Date",
            "friendGenderLabel": "Friend Gender",
            "runAnalysis": "Analyze Result",
            "error_msg": "Wait.. Saju internal engine crashed. Try again.",
            "organ_map": {"Wood": "Liver/Gallbladder", "Fire": "Heart/SI", "Earth": "Stomach/Spleen", "Metal": "Lung/LI", "Water": "Kidney/Bladder"},
            "body_part_map": {"Wood": "Muscles/Eyes", "Fire": "Vessels/Tongue", "Earth": "Skin/Mouth", "Metal": "Respiratory/Nose", "Water": "Bones/Ears"},
            "exercise_map": {"Wood": "Walk/Pilates", "Fire": "HIIT/Dance", "Earth": "Hiking/Strength", "Metal": "Yoga/Boxing", "Water": "Swim/Meditation"},
            "luck_item_map": {"Wood": "Wood/Green", "Fire": "Red/Sun", "Earth": "Yellow/Earth", "Metal": "White/Metal", "Water": "Black/Water"},
            "star_map": {"Wood": "Tree", "Fire": "Sun", "Earth": "Earth", "Metal": "Diamond", "Water": "Ocean"},
            "skill_map": {"Wood": "Planning", "Fire": "Speech", "Earth": "Coordination", "Metal": "Analysis", "Water": "Insight"},
            "element_labels": {"Wood": "Wood", "Fire": "Fire", "Earth": "Earth", "Metal": "Metal", "Water": "Water"},
            "trait_map": {"Wood": "Vitality", "Fire": "Passion", "Earth": "Tolerance", "Metal": "Decision", "Water": "Wisdom"},
            "place_map": {"Wood": "Park", "Fire": "Stage", "Earth": "Cafe", "Metal": "Library", "Water": "Riverside"},
            "season_map": {"Wood": "Spring", "Fire": "Summer", "Earth": "Change of Seasons", "Metal": "Autumn", "Water": "Winter"},
            "flower_map": {"Wood": "Sprout", "Fire": "Flower", "Earth": "Fruit", "Metal": "Seed", "Water": "Root"},
            "industry_map": {"Wood": "Creative/Art", "Fire": "IT/Media", "Earth": "Finance/Real Estate", "Metal": "Tech/Mfg", "Water": "Service/Logistics"},
            "style_map": {"Wood": "Pure", "Fire": "Flashy", "Earth": "Stable", "Metal": "Chic", "Water": "Mystic"},
            "mission_map": {"Wood": "New Challenge", "Fire": "Self-Expression", "Earth": "Finding Balance", "Metal": "Self-Improvement", "Water": "Inner Reflection"},
            "scientific_analysis": "🧬 [Next-Gen Scientific Data Analysis]",
            "element_weight": "Element Energy Weights (100% Ratio)",
            "mbti_dynamic": "MBTI Quad-Letter Psychological Dynamics",
            "rpre_hypothesis": "Persona Hypothesis (RPRE Engine)",
            "REL_LABELS": {
                "A": "Fantastic Duo", "B": "Stable Partner", "C": "Effort Mate", "D": "Unique Combo", "E": "New Challenge Pair"
            },
            "MBTI_TRAITS": {
                "E": "Extroverted", "I": "Introverted", "S": "Realistic", "N": "Intuitive",
                "T": "Logical", "F": "Feeling", "J": "Planned", "P": "Spontaneous"
            },
            "SYNERGY_LABELS": {
                "생": "Synergy", "극": "Conflict", "조화": "Harmony"
            },
            "MISSION_POINTS": ["charm", "special", "twist", "heart-fluttering", "stan-point"],
            "month_names": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            "stage_label": "STAGE"
        },
        "MBTI_FUNC_FRAGMENTS": {
            "e_i": {
                "E": "tends to radiate energy outward and thrive through social interaction,",
                "I": "focuses internal energy to create deep and meaningful results,"
            },
            "n_s": {
                "N": "believes in intuition and future possibilities to pioneer creative paths,",
                "S": "completes perfect stages based on realistic and sensory data,"
            },
            "t_f": {
                "T": "makes logical and objective judgments to establish optimal strategies,",
                "F": "moves hearts through warm empathy and emotional exchange,"
            },
            "j_p": {
                "J": "provides consistent trust with systematic and planned self-management,",
                "P": "enjoys flexible and spontaneous changes, showing sparkling charm anywhere."
            }
        },
        "RPRE_TEMPLATES": {
            "core_v1": "On top of the powerful essence of {p1}, the sophisticated sense of {p2} is added. While the star wears the persona of {mbti} and appears as such to the public, at critical moments, the inherent persistence of {p1} shines through, revealing an 'Iron Fist in a Velvet Glove' style.",
            "hero_v2": "The cosmic base of {p1} provides a rock-solid foundation for {p2}'s creative spark. Publicly known as the {mbti} icon, the star's true strength lies in a hidden '{element}' frequency that only shows when the pressure is at its peak.",
            "mystic_v3": "Guided by {p1}'s intuition and refined by {p2}'s execution, the persona of {mbti} serves as a beautiful mask. Behind it, a complex engine of elemental balance operates, creating a magnetic field that is impossible to ignore."
        },
        "MZ_ANALYSIS_FRAGMENTS": {
            "action_guides": {
                "vibe": [
                    "Build a playlist themed around {idol}'s favorite picks and post it on SNS with your MZ spin.",
                    "Visit a location {idol} recently went to, recreate their photo pose — mini pilgrimage unlocked.",
                    "Find the overlap in your tastes and send {idol} that 'this is literally SO us' signal.",
                    "Style a similar look using {idol}'s personal color or fave fashion pieces. Twins era.",
                    "Write a calligraphy quote from {idol}'s interview that hit hard and post it for the fandom to see.",
                    "Read or watch something {idol} mentioned and drop your own MZ-style review for the timeline."
                ],
                "heart": [
                    "Remember that tiny habit or preference {idol} mentioned — bring it up at a fan sign or fan app. They'll feel SEEN.",
                    "Write them a genuine handwritten letter or message using words that hype up {idol}'s inner strength. Make it real.",
                    "Understand the T/F gap in your MBTIs and prepare the exact kind of words {idol} needs to hear when they're down.",
                    "Collect words that have given {idol} strength and wrap them into an 'encouragement playlist' caption gift.",
                    "Plan a sincere, small celebration not just for their birthday but for their debut anniversary too.",
                    "Edit a short clip capturing all the moments you've watched {idol} grow — send it with nothing but genuine love."
                ],
                "energy": [
                    "Plan a meaningful volunteer event or fan project timed to {idol}'s birthday or anniversary.",
                    "Put together merch or an outfit in {idol}'s personal color — show up and add to the fandom hype.",
                    "Pick up the hobby {idol} recently started, learn it together in spirit. New challenge, new era.",
                    "Create your own challenge video set to {idol}'s song and spread positive energy far and wide.",
                    "Start the same workout {idol} does, log your progress, and share that energy with the universe.",
                    "Leave a bright, warm morning message on {idol}'s fan channel every day. Be their daily sunshine."
                ]
            },

            "relationship_intro": [
                "Your frequency syncs at {score}%! A {rel_label} combo.",
                "Cosmic signals are hitting hard in this {rel_label} chemistry.",
                "Basically destiny, this {rel_label} vibe is undeniable.",
                "Data proves this {rel_label} match is elite, scoring {score}!",
                "Resonance between your waves creates a {rel_label} masterpiece.",
                "A {rel_label} timing across time and space, {score}% probability."
            ],
            "relationship_core": [
                "A perfect textbook relationship where you fill each other's voids.",
                "A narrative of tension and growth, like a coming-of-age drama.",
                "An invincible duo that feels like having the whole world.",
                "Differences act as a catalyst for mutual growth and excitement.",
                "Soul synchronization where a single look says everything.",
                "A positive power combo that can overcome any obstacle with a smile."
            ],
            "bias_essence": [
                "Has a strong '{element}' energy, giving off a charismatic aura.",
                "Dominant '{element}' trait blends sensitivity with stage dominance.",
                "Like a warm sun, is a human vitamin radiating positive energy.",
                "Solid as a rock, a 'Green Flag' icon providing constant trust.",
                "Flexible like clear water, possessing a deep and mysterious charm.",
                "The strength of metal and the brilliance of a gem, shining over time."
            ],
            "bias_point": [
                "The biggest attraction is the gap between charisma and puppy-like vibes.",
                "Fans love the mix of 'Pro Mode' and unexpected daily TMI moments.",
                "A quiet observer whose rare words explode with high dopamine.",
                "Delicate fan love and sharing small daily moments steals hearts.",
                "Trust comes from constant self-improvement and visible growth.",
                "Unrivaled visual sense and unique aesthetic in every outfit."
            ],
            "bias_tmi": [
                "Being {mbti} means they literally live that structured god-tier life — they're out here planning everything while the rest of us are still vibing.",
                "Because of that iconic {mbti} energy, this one memorizes every tiny fan reaction — yes, your tweet from 3 months ago? They saw it. They remember.",
                "That {mbti} personality means they absolutely need solo time to recharge — a certified cat who gives BIG independent main character energy.",
                "Pure {mbti} chaos in the best way: constantly cooking up creative ideas that leave fans shook every single time. Total idea bank era.",
                "On the surface they look calm, but that unexpected {mbti} quirk hits different — they WILL break the silence with something unhinged and iconic.",
                "That {mbti_trait} energy is so real — they low-key become the group therapist and everyone just naturally trusts them with everything."
            ],
            "bias_growth": [
                "The way they level up is actually insane, always finding the most efficient 'XP farm' in life.",
                "They have this hidden grit that only shows up when they are truly passionate about a project.",
                "Growth for them isn't a race; it's about building a solid foundation that never crumbles.",
                "They absorb new skills like a sponge, making every 'side quest' look like a main mission.",
                "Their evolution is constant, serving a new 'era' every time you think you've seen it all.",
                "Resilience is their middle name; they turn every setback into a massive comeback story."
            ],
            "bias_aura": [
                "They carry this 'Main Character' aura that makes the whole room stop and stare.",
                "There's a subtle mystery in their eyes that makes people want to know their deep lore.",
                "They radiate a warm, healing frequency that naturally draws everyone toward them.",
                "A sharp, sophisticated aesthetic that screams 'High-End' even in casual fits.",
                "Their vibe is like a cozy rainy day - calm, deep, and incredibly comforting.",
                "They possess a magnetic field that effortlessly pulls in lucky opportunities."
            ],
            "recent_fortune": [
                "{idol} is in full comeback mode energy. Career high incoming — the stars literally aligned for this moment, no cap.",
                "The interaction luck is going UP. A legendary reaction, an iconic moment with the fandom — it's coming and it's going to be on the timeline forever.",
                "This is a recharging arc, but don't be fooled — the aura is getting DEEPER. When they come back, it's going to be an autumn slay era.",
                "A major career support figure just entered the orbit. An unexpected global collab? The saju says it's not IF, it's WHEN.",
                "{idol}'s finance and brand era is hitting different. Ad deals, solo projects — the bag is being secured. We stan a business girlie/king.",
                "The internal passion is at its absolute peak right now. Whatever {idol} has been creating on their own is about to drop and it will NOT be missed."
            ],
            "synergy_why": [
                "Your '{u_element}' mixed with their '{i_element}' is literally giving unmatched chemistry. The sparks? Absolutely flying. 💥",
                "Your Saju charts literally cover each other's flaws and max out the synergy. You two together? A certified lucky duo. 🍀",
                "The {u_mbti} and {i_mbti} combo covers each other's blind spots with scary precision. It's the most balanced duo on the charts, fr.",
                "'{u_element}' feeding '{i_element}' energy is basically a perfect support-carry dynamic — you are genuinely their power source.",
                "'{u_element}' and '{i_element}' are different flavors that somehow create an addictive chemistry. The rizz is mutual and it's unmatched.",
                "The hustle of {u_mbti} plus the detail-oriented nature of {i_mbti}? Together you're literally unstoppable. Final boss duo."
            ]
        },
        "PURE_LOVE_STYLES": [
            "This person possesses a deep and mysterious inherent energy that cannot be fully captured by conventional personality types. If they feel drawn to you, they will approach you boldly, prioritizing the tremor of their heart and intuitive sparks over rational judgment. They are a wild romantic who entirely yields the intense passion lying dormant within.",
            "Their innate birth month energy uniquely aligns with yours, bringing a profound and stable soul-level belonging, as if connected from a past life, even without words. They exhibit a rock-solid, unwavering affection style, showing serious, unshakeable inner support.",
            "The Yin and Yang of their birth chart perfectly balance yours—providing warmth when you are exhausted and a cooling instinctual balance when you are overheated. Without needing flashy techniques or calculations, they are like a master key for your soul, perfectly fulfilling your emotional voids purely through their natural frequency."
        ],
        "PURE_SYNERGY": {
            "생": "[Harmonious Growth] Their inherent energy acts as a flawless supply line, endlessly nurturing your soul. Simply existing together amplifies positive vibrations, unlocking unprecedented potential and massive fortune—a miraculous cosmic synergy.",
            "극": "[Intense Clash] Your energies sometimes strongly collide, yet this very friction generates a massive creative force that powerfully catalyzes each other's growth. It is a mesmerizing destiny where you complete one another amidst an undeniable, visceral attraction.",
            "비화": "[Mirror Soulmates] A solid bond formed by the union of identical elements. You are partners who create your own vast universe through a deep resonance that requires no explanation. Like twins from a past life, your souls share the same grain, capable of being a lifelong sanctuary."
        },
        "PURE_TIPS": [
            "When approaching them, set aside calculated flirting or textbook strategies. Simply radiate the pure, unfiltered charm of your natural base element (Wood/Fire/Earth/Metal/Water). This is when they will feel the most powerful, undeniable pull toward you.",
            "Rather than heavily staged events or eloquent conversational skills, the cosmic frequencies of you two perfectly synchronize during moments of shared physical presence—like silently gazing at the night sky or walking through nature.",
            "Instead of being swayed by their exterior or situational factors, show them consistent trust, as if piercing through to the essence of their soul. Sending them unconditional and silent inner support is the absolute master key to opening the deep doors of their heart."
        ],
        "EXPERT_ADVICE": {
            "Health": [
                "Agent A (Traditional): Your element suggests a weakness in the {organ} area. Traditional K-Saju recommends warm herbal teas to balance your internal energy.",
                "Agent B (Psychological): Stress tends to manifest in your {body_part}. Prioritize 'Zen moments' and deep meditation to prevent burnout.",
                "Agent C (Trend): Try {exercise}, currently trending in Seoul. It's the perfect flow to circulate your specific energy type."
            ],
            "Wealth": [
                "Agent A (Legacy): A strong financial alignment occurs in Month {month}. This is your window for long-term investments.",
                "Agent B (Behavioral): You tend to spend impulsively when your energy is high. Set a 'Delay Rule' for big purchases.",
                "Agent C (Tech): Using a {luck_item} themed wallet or digital asset will act as a 'Luck Magnet' for your secondary income."
            ],
            "Career": [
                "Agent A (Authority): Your chart shows 'The {star}' energy. You're a natural-born leader destined for high-level management.",
                "Agent B (Social): Your networking style is your sharpest weapon. Focus on 'Soft Power' to win over difficult colleagues.",
                "Agent C (Skill): Leveling up in {skill} is your 2026 cheat code. This specific synergy will trigger a massive career pivot."
            ],
            "Love": [
                "Agent A (Destiny): You have a fated connection with someone carrying 'The {element}' energy. They are your missing puzzle piece.",
                "Agent B (Aura): Your ultimate rizz is your '{trait}'. Lean into it during first dates—it's what makes you unforgettable.",
                "Agent C (Vibe): A high-probability encounter is predicted at a {place}. Keep your 'Main Character' energy high when you visit."
            ]
        },
        "LIFETIME_EXPERTS": [
            {
                "name": "Master Cheong",
                "focus": "Grand Cycle & Elemental Balance",
                "comment": "Your destiny flows with the energy of {season}. Like a great river, you will overcome obstacles and reach your vast ocean of success in the latter half of life."
            },
            {
                "name": "Dr. Jung",
                "focus": "Inner Temperament & Emotional Flow",
                "comment": "You have the delicate soul of a {flower}. Never doubt your unique frequency; your sensitivity is actually your greatest power in this chaotic world."
            },
            {
                "name": "Neo",
                "focus": "Modern Tech Aptitude & Wealth Logic",
                "comment": "Your energy algorithm is optimized for the {industry} sector. You possess the 'Analytical Eye' that identifies hidden wealth before others can even see it."
            },
            {
                "name": "Sophie",
                "focus": "Relationship Depth & Soul Resonance",
                "comment": "In love, you serve '{style}' vibes. You might struggle to express feelings, but once you commit, you are a legendary partner with unshakeable loyalty."
            },
            {
                "name": "Zen Master",
                "focus": "Life Mission & Holistic Alignment",
                "comment": "Your ultimate mission isn't just success, but '{mission}'. Your clear aura will naturally guide others and create a positive butterfly effect around you."
            }
        ],
        "TIP_COMPONENTS": {
            "actions": [
                "Lead with authentic {mbti} honesty instead of playing mind games",
                "Channel the mutual {u_el} energy in a direction that uplifts each other",
                "Plan an unexpected surprise event at {place}",
                "Respect their little {mbti_trait} quirks — that's where the magic lives",
                "Enjoy some one-on-one {exercise} sessions together",
                "Time your vibes to align when {star} energy is peaking",
                "Drop some unexpected {mbti}-coded humor every once in a while",
                "Keep that steady, textbook {mbti_trait} main character energy",
                "Show up with the star's fave {luck_item} — understood the assignment",
                "Flex your expert-level {skill} and let them notice",
                "Give big genuine reactions — that's your rizz",
                "Prioritize mindful {organ} care first — wellness is the glow-up",
                "Go on a pilgrimage together to {place} holy sites",
                "Write a heartfelt letter praising star's {trait} — no crumbs left",
                "Maintain that signature cool {mbti} aura that makes you iconic"
            ],
            "topics": [
                "complimenting the star's magnetic {trait} energy",
                "leveraging the {u_el}/{i_el} elemental synergy between you two",
                "checking on their {organ} wellness before anything else",
                "activating the star's cherished {luck_item} for good vibes",
                "sharing real, thoughtful advice about {skill}",
                "proposing a tour of {place} together",
                "exchanging each other's {star} fortune readings",
                "hyping up the star's {mbti_trait} side — they need to hear it",
                "bringing up that iconic {trait} keyword from an old interview",
                "spilling the tea on the star's #1 {luck_item} obsession",
                "proposing a duo {exercise} challenge between you two",
                "gifting a lucky color item matching star's {u_el} energy"
            ],
            "results": [
                "the ultimate cheat code to flood the relationship with dopamine.",
                "the secret to syncing your soul frequencies on the same wavelength.",
                "the path to planting an unshakeable green flag of certainty.",
                "the move that tightens the fate string that's existed since past lives.",
                "the fastest shortcut to becoming their #1 person.",
                "the final puzzle piece that completes your exclusive chemistry.",
                "the way to create god-tier synergy that makes hearts race.",
                "the method to level up into each other's destined main characters.",
                "the ultimate signal that answers the star's unspoken opening line.",
                "the strategy to amplify your {rel_type} synergy by 200%."
            ]
        },
        "GEN_MISSION_COMPONENTS": {
            "actions": {
                "E": [
                    "Sharing a {target} proof shot in the community", "Pushing the agenda of the star's {trait} to besties", 
                    "Participating in a public SNS challenge", "Doing a live pilgrimage to a energetic {place}",
                    "Creating and sharing a {mbti} meme of the star", "Running an {exercise} challenge with fellow fans",
                    "Dropping by the star's birthday ad for a pic", "Brainstorming for group-order merch",
                    "Filming yourself screaming the fanchant to the new bop", "Simping over a {point} eye-contact moment with the star"
                ],
                "I": [
                    "Quietly journaling with a {target}", "Binge-watching the star's past {trait} fancams",
                    "Having alone time at the {place} the star mentioned", "Meditating to the star's playlist",
                    "Writing a heartfelt letter to the star", "Secretly hoarding the star's {luck_item}",
                    "Keeping a private log of the star's {mbti} daily life", "Having a fancam marathon at home",
                    "Analyzing the star's {star} fortune as a lucky charm", "Writing down the warm comforting words the star said"
                ]
            },
            "targets": {
                "Wood": ["green sprout-themed merch", "forest-scented pilgrimage spot", "video of their growth era", "green lucky item"],
                "Fire": ["bold red colored item", "fiery stage fancam", "dazzling night view spot", "scene of burning passion"],
                "Earth": ["aesthetically pleasing beige merch", "calming earthy place", "photo of the star's daily life", "record of their silent hard work"],
                "Metal": ["chic silver accessory", "sharp charismatic photoshoot", "minimalist designed place", "interview showing their iron will"],
                "Water": ["photocard with a blue ocean vibe", "calming rainy radio session", "slow song with a deep afterglow", "clear and transparent vibe item"]
            },
            "contexts": [
                "Amplify your {rel_type} synergy by 200%!", "Enjoy the moment your destined frequencies sync.",
                "Make the invisible thread from your past life even stronger.", "The fastest shortcut to becoming their #1.",
                "Complete the ultimate green flag.", "Sync your energy to the star's {u_el} vibe.",
                "The final puzzle to your secret chemistry.", "Experience the god-tier synergy that makes your heart race.",
                "Become the ultimate bestie.", "The magic to turn your differences into a {point} charm."
            ]
        },
        "MISSION_COMPONENTS": {
            "labels": [
                "{u_mbti} x {i_mbti} Stage {n} Mission",
                "{u_el} & {i_el} Energy Fusion",
                "Escape the Stan Denial Era: {point}",
                "Unlock the Main Character Buff: {point}",
                "Destiny Frequency Sync",
                "Custom {i_mbti} Strategy Guide",
                "Break the Chemistry Ceiling: {point}",
                "Soul Bestie Selfie Proof",
                "Dopamine Full Charge Mission",
                "God-Tier Synergy Routine",
                "Escape the Past Life Parking Lot: {point}",
                "Unlock Star's Unique {trait} Force Field",
                "Walk the {rel_type} Flower Path Together"
            ],
            "reasons": [
                "In K-saju, {u_el} creates and supports {i_el} — that's your blueprint.",
                "Your {u_mbti}'s {mbti_trait} energy is a fresh stimulant that resonates with the star.",
                "This bridges the tension point where your {organ} energies clash.",
                "It's the solution to fix the subtle misalignment found in your past life chart.",
                "The star's {star} energy is literally resonating with your {u_el} frequency right now.",
                "This pushes the {rel_type} synergy between you two to its absolute peak.",
                "The star's {mbti} vibe is lowkey obsessed with your {mbti_trait} energy."
            ],
            "tasks": {
                "vibe": [
                    "Create custom merch centered around star's iconic {trait}",
                    "Decorate your journal with photo cards featuring your {mbti} compatibility score",
                    "Recreate a photo at {place} that the star once mentioned in the same exact pose",
                    "Actually learn the {skill} the star is currently obsessed with",
                    "Flex a {luck_item} that matches the star's personal color palette",
                    "Write out the star's most iconic quote in calligraphy and share it",
                    "Stream the star's new stage performance {n} times and post proof",
                    "Create a viral meme about the star's everyday {mbti}-coded moments"
                ],
                "heart": [
                    "Mass tag the SNS hashtag to support the star's {organ} health",
                    "Send a heartfelt support message that's authentically {mbti_trait}",
                    "Gift an item similar to star's treasured {luck_item}",
                    "Write calligraphy praising the star's mesmerizing {star} aura",
                    "Binge the star's debut era {trait} videos to reconnect with the origin story",
                    "Send the exact warm words of comfort the star deserves to hear",
                    "Write a handwritten letter analyzing the star's {mbti} personality and post it",
                    "Give yourself a self-appreciation moment for patiently supporting star's growth"
                ],
                "energy": [
                    "Post your workout proof with the mindset of doing {exercise} together with the star",
                    "Dress in a lucky color that aligns with the star's {i_el} energy",
                    "Edit a {n}-minute video capturing the star's epic growth narrative",
                    "Trust your {u_el}/{i_el} synergy and take on a new personal goal challenge",
                    "Meditate to the star's playlist and cleanse your energy field",
                    "Live your best life like the star would — log it and share proof",
                    "Flex your daily outfit featuring star's {star} lucky item",
                    "Spread the word about star's {trait} magic to at least one person today"
                ]
            }
        },
        "SYNERGY_MISSIONS": {
            "analysis_1": {
                "label": "Deep Vibe: {point_1} 📸",
                "boost": 15,
                "reason": "Deep taste analysis based on {reason_1}.",
                "tasks": ["{task_1_1}", "{task_1_2}", "{task_1_3}"]
            },
            "analysis_2": {
                "label": "Soul Sync: {point_2} 💬",
                "boost": 15,
                "reason": "Soul resonance through {reason_2} signals.",
                "tasks": ["{task_2_1}", "{task_2_2}", "{task_2_3}"]
            },
            "analysis_3": {
                "label": "Cosmic Action: {point_3} 🎡",
                "boost": 20,
                "reason": "Synergy boost action to solve {reason_3}.",
                "tasks": ["{task_3_1}", "{task_3_2}", "{task_3_3}"]
            }
        },
        "MZ_SAJU_DICTIONARY": {
            "일주": "The energy of the day you were born! It's the core 'vibe' of your Saju chart, representing your true self.",
            "용신": "Your ultimate 'lucky charm' energy. Amplifying this lowers life's difficulty level instantly!",
            "기구신": "The subtle 'villain' energy in your chart. Manage it well to protect your peace.",
            "상생": "A mutually supportive, ultimate bestie dynamic. The definition of 'we just click'.",
            "상극": "A spicy chemistry where friction creates massive, unstoppable energy.",
            "도화살": "Main character energy. A natural 'stan attractor' vibe that makes everyone look at you.",
            "역마살": "Global wanderer energy. You can't stay still, and movement brings you massive success!",
            "현침살": "The ultimate 'fact-checker'. Sharp insight and unmatched attention to detail.",
            "비견": "Soulmate colleague energy. Increases your reliable mutuals and squad size.",
            "겁재": "A competitive drive. Having a little rivalry actually makes you glow up faster!",
            "편인": "The quirky 'idea bank'. Out-of-the-box thinking that becomes your unique charm.",
            "정인": "Born to be loved. The ultimate 'maknae' vibe who naturally receives affection wherever they go.",
            "식신": "Overflowing talent and good food luck. The ultimate productive and enjoying-life 'god-saeng' vibe.",
            "상관": "The rebellious innovator energy. Breaks the rules and hates being boxed in—pure creative chaos!",
            "편재": "Unexpected jackpot energy. Big scale flexers looking for that massive payout.",
            "정재": "The steady, reliable 'human ledger' energy. Slowly but surely building an empire.",
            "편관": "Charismatic leader energy born from overcoming extreme trials. High risk, legendary rewards.",
            "정관": "The textbook rule-follower. A principled, unshakable straight-A student vibe."
        }
    },
    "ko": {
        "ENERGY_TRAITS": {
            "Wood": {
                "name": "성장하는 나무(Wood) 🌲",
                "desc_intro": [
                    "당신의 영혼은 끝없이 뻗어 나가는 '큰 나무(거목)'의 에너지를 품고 태어났습니다. 명리학에서 목(木) 기운은 생명력, 호기심, 그리고 굽히지 않는 성장 욕구를 의미합니다.",
                    "싹을 틔우고 쑥쑥 자라나는 새싹처럼, 무한한 가능성과 시작의 파동을 가진 목(木) 기운을 타고났습니다."
                ],
                "desc_core": {
                    "E": [
                        "완벽한 인싸 재질이자 자기계발 폼이 미친 '갓생러'입니다. 세상의 모든 것에 흥미를 느끼며, 시작하는 것을 두려워하지 않는 추진력의 아이콘이죠. 때로는 오지랖이 넓다는 소리를 듣기도 하지만, 그 이면에는 사람을 향한 따뜻한 애정과 '다 같이 잘 헤쳐 나가자'는 긍정적인 포용력이 자리 잡고 있습니다.",
                        "가만히 있지 못하고 끊임없이 새로운 일을 벌이는 에너자이저! 당신 주위에는 늘 사람이 끊이지 않으며 특유의 오지랖으로 주변을 긍정적으로 변화시킵니다."
                    ],
                    "I": [
                        "조용하지만 내면의 성장을 향한 욕구가 누구보다 강렬한 외유내강형 인간입니다. 하나의 관심사에 딥다이브하며 조용히 실력을 키워나가는 대기만성형 갓생러입니다.",
                        "겉으로는 유연해 보이지만 당신의 신념을 건드리는 순간 거목처럼 굳건하게 맞서는 고집이 숨어 있습니다. 혼자만의 시간을 통해 나이테를 단단하게 새기는 타입입니다."
                    ],
                    "default": [
                        "완벽한 인싸 재질이자 자기계발 폼이 미친 '갓생러'입니다. 세상의 모든 것에 흥미를 느끼며, 시작하는 것을 두려워하지 않는 추진력의 아이콘이죠. 때로는 오지랖이 넓다는 소리를 듣기도 하지만, 그 이면에는 사람을 향한 따뜻한 애정과 '다 같이 잘 헤쳐 나가자'는 긍정적인 포용력이 자리 잡고 있습니다.\n\n기본적으로 유연해 보이지만, 당신의 신념을 건드리는 순간 거목처럼 굳건하게 맞서는 고집(자존심)도 숨어 있습니다. 이 고집이 당신을 지탱하는 강력한 무기이자 매력 포인트입니다."
                    ]
                },
                "desc_career": [
                    "[직업 및 라이프스타일]\n한자리에 가만히 있는 것보다는 끊임없이 새로운 프로젝트를 기획하고, 사람들과 교류하며 아이디어를 팽창시키는 직무가 찰떡입니다. 스타트업 창업, 에디터, 크리에이터, 기획자 등 '무에서 유를 창조하는' 역할에서 도파민을 강력하게 느낍니다. 워라밸보다는 역동적인 성취감이 영혼을 춤추게 합니다.",
                    "[직업 및 라이프스타일]\n성장과 교육에 관련된 분야에서 도파민을 강력하게 느낍니다. 누군가를 가르치거나 멘토링하는 역할, 혹은 생동감 넘치는 스타트업 무대가 당신의 성장을 돕습니다."
                ],
                "desc_advice": [
                    "[운명 개척 액션 플랜]\n시작은 거창하나 마무리가 흐지부지될 위험(용두사미)이 항상 도사리고 있습니다. 나무가 예쁘게 자라려면 주기적인 가지치기가 필수이듯, 관심사를 좁히고 하나의 목표에 딥다이브하는 연습이 필요합니다.",
                    "[운명 개척 액션 플랜]\n바람에 흔들리는 것을 두려워하지 마세요. 가끔은 실패하더라도 꺾이지 않고 다시 새순을 돋게 하는 당신만의 탄력성이 가장 큰 무기입니다."
                ]
            },
            "Fire": {
                "name": "불타오르는 불(Fire) 🔥",
                "desc_intro": [
                    "당신의 영혼은 세상을 밝게 비추는 '태양' 혹은 어둠 속의 '횃불' 에너지를 품고 태어났습니다. 명리학에서 화(火) 기운은 열정, 확산, 화려함, 그리고 감정을 숨기지 못하는 투명함을 의미합니다."
                ],
                "desc_core": {
                    "E": [
                        "어디를 가나 시선을 강탈하는, 존재 자체가 플러팅인 '핵인싸'입니다. 텐션이 기본적으로 MAX에 맞춰져 있으며, 리액션이 혜자스러워 주변 사람들에게 에너지를 마구 퍼주는 충전기 같은 존재입니다. 겉과 속이 매우 투명해서 뒤끝이 없고, 화가 나더라도 불꽃처럼 확 타올랐다가 금세 가라앉는 '마라맛 쿨톤' 성격입니다."
                    ],
                    "I": [
                        "겉으로는 차분해 보일 수 있으나 내면에는 활활 타오르는 거대한 불꽃을 숨기고 있습니다. 나를 인정해주는 좁고 깊은 관계에서만 내면의 화력을 폭발시키는 따뜻한 화로같은 사람입니다."
                    ],
                    "default": [
                        "어디를 가나 시선을 강탈하는, 존재 자체가 플러팅인 '핵인싸'입니다. 텐션이 기본적으로 MAX에 맞춰져 있으며, 리액션이 혜자스러워 주변 사람들에게 에너지를 마구 퍼주는 충전기 같은 존재입니다.\n\n불의 에너지는 '예의'와 '명예'를 중시합니다. 나를 인정해 주는 사람 앞에서는 한없이 따뜻하지만, 선을 넘는 사람에게는 가차 없이 불벼락을 내리는 단호함도 갖추고 있습니다."
                    ]
                },
                "desc_career": [
                    "[직업 및 라이프스타일]\n무대 체질이며 스포트라이트를 받아야 잠재력이 터집니다. 연예인, 방송 관련 직무가 완벽한 시너지를 냅니다."
                ],
                "desc_advice": [
                    "[운명 개척 액션 플랜]\n감정 기복이 심해 가끔 급발진을 할 때가 있습니다. 화가 났을 때는 '3초 심호흡' 후 말하는 습관을 들이세요."
                ]
            },
            "Earth": {
                "name": "단단한 흙(Earth) ⛰️",
                "desc_intro": [
                    "당신의 영혼은 만물을 온화하게 품어주는 '광활한 대지'의 에너지를 품고 태어났습니다. 명리학에서 토(土) 기운은 중재, 포용력, 신용을 의미합니다."
                ],
                "desc_core": {
                    "E": [
                        "주변 사람들이 믿고 기대는 든든한 '인간 보조배터리'입니다. 어디 치우치지 않는 평정심이 당신의 최대 무기입니다."
                    ],
                    "I": [
                        "무심한 척 챙겨주는 츤데레 매력이 돋보이며, 한 번 내 사람이라 생각하면 끝까지 품고 가는 의리파입니다."
                    ],
                    "default": [
                        "주변 사람들이 믿고 기대는 든든한 '인간 보조배터리'입니다. 토 기운을 가진 사람이 진짜 화를 내면 지진이 일어나는 것과 같아서 주변이 초토화될 수 있습니다."
                    ]
                },
                "desc_career": [
                    "[직업 및 라이프스타일]\n리스크를 즐기기보다는 차곡차곡 쌓아 올리는 것을 선호합니다. 인사, 교육, 금융 분야의 GOAT입니다."
                ],
                "desc_advice": [
                    "[운명 개척 액션 플랜]\n남들을 챙기느라 정작 자신은 못 챙길 때가 많습니다. 자신을 1순위로 두는 연민이 가끔 필요합니다."
                ]
            },
            "Metal": {
                "name": "날카로운 쇠(Metal) ⚔️",
                "desc_intro": [
                    "당신의 영혼은 단단한 '순백의 보석' 혹은 '날카로운 검'의 에너지를 품고 태어났습니다. 명리학에서 금(金) 기운은 결단력과 냉철한 이성을 의미합니다."
                ],
                "desc_core": {
                    "E": [
                        "호불호가 명확하고, 맺고 끊음이 칼 같은 '확신의 T' 성향이 강합니다. 논리와 팩트가 확실할 때만 마음을 엽니다."
                    ],
                    "I": [
                        "겉보기엔 다가가기 힘든 얼음장벽 같지만, 사실 내면에게는 '내 사람'을 끔찍이 아끼는 뜨거운 의리가 숨어 있습니다."
                    ],
                    "default": [
                        "호불호가 명확하고 맺고 끊음이 칼 같은 스타일입니다. 겉바속촉의 정석으로, 당신의 바운더리 안에 들어온 사람에게는 인생을 걸고 지켜줍니다."
                    ]
                },
                "desc_career": [
                    "[직업 및 라이프스타일]\n정확한 수치와 규칙이 있는 분야에서 빛을 발합니다. IT 딥테크, 의료, 법률 분야의 에이스입니다."
                ],
                "desc_advice": [
                    "[운명 개척 액션 플랜]\n스스로에 대한 기준이 너무 높아 완벽주의의 늪에 빠질 수 있습니다. 가끔은 빈틈을 보여주는 유연함을 가져보세요."
                ]
            },
            "Water": {
                "name": "자유로운 물(Water) 🌊",
                "desc_intro": [
                    "당신의 영혼은 형체가 없으나 어디든 흘러가는 '깊고 푸른 바다'의 에너지를 품고 태어났습니다. 명리학에서 수(水) 기운은 지혜와 유연성을 의미합니다."
                ],
                "desc_core": {
                    "E": [
                        "상황에 맞춰 자유자재로 모습을 바꾸는 적응력의 끝판왕입니다. 어떤 환경에서도 부드럽게 스며드는 엄청난 소셜 스킬이 강점입니다."
                    ],
                    "I": [
                        "생각의 깊이가 남다르고, 통찰력이 뛰어나서 본질을 꿰뚫어 보는 '철학자'의 면모를 가졌습니다."
                    ],
                    "default": [
                        "적응력의 끝판왕이자 생각의 깊이가 태평양급입니다. 겉으로는 유약해 보일지 몰라도, 바위도 뚫어버리는 물방울처럼 은근한 끈기가 장난 아닙니다."
                    ]
                },
                "desc_career": [
                    "[직업 및 라이프스타일]\n시간과 공간에 얽매이지 않고 자유롭게 사고를 전개하는 분야가 제격입니다. 창작자, 기획자, 자유직업군이 찰떡입니다."
                ],
                "desc_advice": [
                    "[운명 개척 액션 플랜]\n생각이 너무 많아서 실천력이 떨어질 수 있습니다. 일단 생각은 멈추고 밖으로 나가 몸을 움직이는 'JUST DO IT' 정신이 생존 전략입니다."
                ]
            }
        },
        "MONTH_FORTUNES": {
            "1": {
                "theme": "새로운 시작의 기운, '{dominant}' 에너지 🌱",
                "signal": "{idol}님과 함께 새해 목표를 세우기 가장 좋은 달! 시너지가 폭발합니다.",
                "guide": "갓생 모드 활성화! 하루 10분 독서나 운동으로 시작하세요. 일상 속 금전운이 조금씩 상승합니다."
            },
            "2": {
                "theme": "지적 성취 & 깊은 몰입 📚",
                "signal": "{idol}님의 지적인 면모에 영감을 받게 됩니다. 깊이 있는 소통의 기회 혹은 간접적인 깨달음이 올 수 있어요.",
                "guide": "배움에 투자하세요. 새로운 자격증이나 공부, 혹은 그동안 미루던 취미가 큰 자산이 됩니다."
            },
            "3": {
                "theme": "봄날의 생기 & 사교적 확장 🌸",
                "signal": "{idol}님과 관련된 오프라인 이벤트나 친구들과 함께 외출하기 딱 좋은 타이밍!",
                "guide": "생명력이 깨어나는 시기, 새로운 인연이 찾아옵니다. 모임에 적극적으로 참여하세요. 💓 대인관계 운 UP!"
            },
            "4": {
                "theme": "열정의 에너지 & 성장 가속도 🔥",
                "signal": "{idol}님의 식지 않는 열정이 당신의 훌륭한 원동력이 됩니다. 함께 새로운 도전에 나서보세요!",
                "guide": "고민만 하던 거창한 목표들을 당장 시작하세요. 눈에 띄는 실행력이 최종 성과를 크게 좌우합니다."
            },
            "5": {
                "theme": "안정의 구축 & 내면의 평화 ⛰️",
                "signal": "잠시 달리기를 멈추고 편안하게 휴식하며 {idol}님과 깊은 유대감을 쌓기 좋은 달입니다.",
                "guide": "주변 환경과 책상을 깔끔하게 정리하세요. 청결한 공간에서 좋은 기운과 운세가 원활하게 흐릅니다."
            },
            "6": {
                "theme": "소통의 폭발 & 창의적 아이디어 💡",
                "signal": "이번 달에는 {idol}님의 즐거운 소식이나 깜짝 스포일러, 의외의 소통을 기대해도 좋아요.",
                "guide": "순간적으로 스쳐가는 아이디어를 놓치지 말고 모두 기록하세요. 작은 메모가 거대한 프로젝트로 이어집니다."
            },
            "7": {
                "theme": "감정의 고조 & 직관력의 절정 🌊",
                "signal": "{idol}님과의 운명적 주파수가 강렬하게 진동합니다. 완벽하게 스며드는 덕통사고, 힐링 타임!",
                "guide": "상황의 유불리를 따지기보다 당신의 직관을 믿고 베팅하세요. 내면 깊은 영혼의 나침반이 이미 정답을 알고 있습니다."
            },
            "8": {
                "theme": "결실의 서막 & 풍요를 위한 준비 ⚔️",
                "signal": "{idol}님의 눈에 띄는 커리어적 성취를 함께 축하하며 엄청난 긍정 에너지를 교류하세요.",
                "guide": "자잘한 외부 활동보다는 당신의 건강 관리에 집중하세요. 규칙적인 루틴과 헬스 케어가 당신의 기본 체급(Base Stat)을 올립니다."
            },
            "9": {
                "theme": "냉철한 판단 & 목표 재설정 🎯",
                "signal": "{idol}님의 행보에 발맞추어 함께 하반기 및 연말 계획을 꼼꼼하게 점검하고 마음을 다잡는 시기입니다.",
                "guide": "자산과 재정 흐름을 한 치의 오차 없이 점검하세요. 불필요한 나쁜 습관과 지출을 칼같이 잘라야 더 큰 기회를 잡습니다."
            },
            "10": {
                "theme": "깊은 이해 & 정신적 성장 🔮",
                "signal": "가을이 무르익고, 오늘은 {idol}님의 깊이 숨겨진 철학적 메시지나 진심을 깊이 이해하게 될 것입니다.",
                "guide": "매일 밤 꾸준한 명상이나 조용한 일기 쓰기로 내면을 거울처럼 직면하세요. 스스로의 진짜 목소리에 응답할 때 큰 운이 터집니다."
            },
            "11": {
                "theme": "변화의 파도 & 유연한 전략 🌊",
                "signal": "{idol}님의 과감한 스타일 변신이나 대담한 시도를 응원하며 당신도 엄청난 우주적 용기의 기운을 전달받습니다.",
                "guide": "자연스러운 흐름의 파도에 몸을 유연하게 맡기세요. 예기치 않은 변화를 전혀 두려워하지 않고 즐길 때 비로소 한 단계 도약합니다."
            },
            "12": {
                "theme": "완성과 휴식, 새로운 꿈을 향해 ❄️",
                "signal": "{idol}님을 향한 충만한 사랑과 감사로 가득한 마음으로, 차분하게 한 해를 따뜻하게 덮고 마무리하는 포근한 달입니다.",
                "guide": "수고한 나 자신만을 위한 따뜻한 힐링타임! 연말에 나에게 주는 작은 보상이 단단한 내년의 에너지로 치환됩니다."
            }
        },
        "EXPERT_ADVICE": {
            "Health": [
                "에이전트A(전통파): 이 오행은 {organ}의 기운이 약해지기 쉬우니 평소 따뜻한 차로 기운을 보강해야 합니다. 특히 환절기에 기력이 급격히 떨어질 수 있으니 주의하세요.",
                "에이전트B(심리파): 스트레스가 {body_part}로 전이될 수 있습니다. 억지로 참기보다는 소리 내어 울거나 크게 웃는 감정 배출이 사주적 치유법입니다.",
                "에이전트C(트렌드파): 요즘 유행하는 {exercise}로 기운을 순환시키세요. 당신의 오행은 '정적인 에너지'를 '동적인 활동'으로 전환할 때 건강운이 살아납니다."
            ],
            "Wealth": [
                "에이전트A(자산가): {month}월에 재물 합이 들어오니 투자는 이때를 노리세요. 땅이나 문서와 관련된 운이 강하니 장기적인 안목이 필요합니다.",
                "에이전트B(경제학자): 소비 성향이 감정적일 때가 많으니 '장바구니 24시간 대기' 규칙을 만드세요. 계획에 없는 지출이 운의 흐름을 막고 있습니다.",
                "에이전트C(테크핀): {luck_item} 오브제를 책상 서북쪽에 두면 금전적 기회가 찾아올 것입니다. 디지털 자산보다는 실물 기반의 투자가 더 안정적입니다."
            ],
            "Career": [
                "에이전트A(멘토): 당신의 사주에는 {star}의 기운이 있어 리더로서의 자질이 충분합니다. 2026년은 하반기에 큰 승진의 기회가 열려 있습니다.",
                "에이전트B(헤드헌터): 조직 내에서의 소통 방식만 조금 유연하게 바꾼다면 승진운이 따릅니다. 특히 선배보다는 후배들의 지지를 얻는 것이 핵심입니다.",
                "에이전트C(코치): {skill} 분야의 자기계발이 2026년 커리어 떡상을 결정짓는 치트키입니다. 남들이 가지 않는 틈새 시장을 노리는 전술이 유효합니다."
            ],
            "Love": [
                "에이전트A(매칭커플): {element} 기운을 가진 사람과 천생연분입니다. 서로를 보완해주는 상생의 관계가 형성되어 고난도 쉽게 헤쳐 나갈 수 있습니다.",
                "에이전트B(연애술사): 당신의 매력 포인트는 {trait}입니다. 억지로 꾸미기보다 본연의 기운을 드러낼 때 이성의 마음을 더 강력하게 흔들 수 있습니다.",
                "에이전트C(커플매니저): {place}에서의 우연한 만남이 깊은 인연으로 이어질 확률이 높습니다. 평소와 다른 동선으로 움직여보세요. 인연은 예기치 못한 곳에서 옵니다."
            ]
        },
        "LIFETIME_EXPERTS": [
            {
                "name": "마스터 청 (정통 명리학자)",
                "focus": "대운의 흐름과 오행의 균형",
                "comment": "당신의 운명은 {season}의 기운을 타고났습니다. 굴곡은 있겠으나 결국 거대한 강물처럼 목표에 도달할 대기만성형 사주입니다."
            },
            {
                "name": "닥터 정 (심리 사주 상담사)",
                "focus": "내면의 기질과 정서적 패턴",
                "comment": "겉으로는 강해 보이지만 속은 섬세한 {flower} 같은 영혼입니다. 본인의 재능을 의심하지 마세요. 당신은 이미 충분히 빛나고 있습니다."
            },
            {
                "name": "네오 (데이터 기반 사주 분석가)",
                "focus": "현대적 직업 적성과 재물 형성 패턴",
                "comment": "당신의 사주 알고리즘은 {industry} 분야에서 최적의 성능을 발휘합니다. 실리적인 판단력이 뛰어나 자산 형성이 빠른 타입입니다."
            },
            {
                "name": "소피 (관계 및 연애 스페셜리스트)",
                "focus": "인연의 깊이와 소통의 기술",
                "comment": "사랑에 있어 당신은 {style} 스타일입니다. 진심을 전하는 데 서툴 수 있지만, 한 번 맺은 인연은 끝까지 지키는 순애보적인 면모가 매력입니다."
            },
            {
                "name": "젠 마스터 (홀리스틱 라이프 코치)",
                "focus": "삶의 미션과 전체적인 에너지 케어",
                "comment": "인생의 목적은 단순히 성공하는 것이 아니라 {mission}에 있습니다. 당신의 맑은 기운이 주변 사람들에게도 긍정적인 영향을 미칠 것입니다."
            }
        ],
        "LOVE_STYLES": [
            "여우 재질 만렙. 겉으로는 쿨내 나는데 사실 다 보고 있음.",
            "골든 리트리버 그 잡채! 당신만 보면 텐션 폭발.",
            "츤데레의 정석. 당신한테만 무장해제되는 갭모에.",
            "확신의 그린플래그. 깊은 밤 통화가 제일 즐거움.",
            "길고양이 모드. 한 번 마음 열면 당신 곁을 안 떠남."
        ],
        "ELEMENT_SYNERGY": {
            "생": "[갓벽조합] 서로의 영혼을 채워주는 미친 시너지.",
            "극": "[매운맛 케미] 서로 다르지만 그래서 더 끌리는 사이.",
            "비화": "[찐친 바이브] 말 안 해도 통하는 소울메이트."
        },
        "TIPS": [
            "밀당은 절대 금지! 솔직한 직진만이 상대방의 마음을 여는 유일한 패스워드입니다.",
            "뻔한 데이트는 지루함의 상징. 예상치 못한 장소나 활동으로 도파민을 강력하게 선사하세요.",
            "무한 칭찬 지옥으로 초대하세요! 상대방의 사소한 변화를 알아차리고 언급하는 것이 핵심입니다.",
            "집착은 최대의 레드플래그. 나만의 '갓생'을 사는 당당한 모습이 상대에게는 더 매력적으로 다가옵니다.",
            "디테일한 취향 저격 선물을 준비하세요. 스타가 예전에 흘리듯 말했던 아이템이라면 감동 200%.",
            "미스터리함을 유지하세요. 당신의 모든 정보를 한 번에 공개하지 말고 천천히 보여주는 것이 팁입니다.",
            "시각적인 시그널을 보내세요. 세련된 스타일링이나 감각적인 일상 사진 공유가 호감도를 높입니다.",
            "말보다 행동이 중요합니다. 상대방이 번거로워하는 일을 조용히 챙겨주는 모습에 심쿵할 거예요.",
            "가끔은 취약한 모습도 보여주세요. 완벽한 모습 뒤의 인간미가 서로를 더 가깝게 연결해줍니다.",
            "든든한 편이 되어주세요. 고민을 들어줄 때 공감과 지지를 아끼지 않는 것이 가장 큰 위로입니다.",
            "둘만의 시그니처 루틴을 만드세요. 작은 습관 하나가 관계를 특별하게 만드는 치트키가 됩니다.",
            "적절한 스킨십은 관계의 촉매제. 상황에 맞는 자연스러운 제스처로 설렘 지수를 높여보세요.",
            "상대방의 개인 시간을 존중하세요. 적당한 거리가 오히려 서로를 더 갈망하게 만듭니다.",
            "함께 성장하는 파트너가 되세요. 서로의 목표를 응원하며 함께 레벨업하는 시너지를 즐기세요.",
            "위트 있는 대화로 폼을 유지하세요. 적절한 농담과 티키타카는 관계의 활력소입니다."
        ],
        "MISSION_FRAGMENTS": {
            "labels": [
                "갓벽한 취향 공유: {point} 📸", "영혼의 딥다이브 토크: {point} 💬", "도파민 힐링 데이트: {point} 🎡",
                "우주적 감성 동기화: {point} ✨", "주인공 에너지 싱크: {point} 🌟", "숨겨진 로어 해제: {point} 🔑"
            ],
            "reasons": [
                "서로의 {u_el}와 {i_el} 에너지가 만나 생기는 독특한 자기장 때문입니다.",
                "{u_mbti}와 {i_mbti} 사이의 심리적 소통 간극을 분석한 결과입니다.",
                "운명적으로 설정된 두 사람만의 영혼 주파수를 동기화하는 단계입니다.",
                "오행의 흐름을 최적화하여 완벽한 서포트-캐리 다이내믹을 형성합니다.",
                "전체적인 사주 차트에서 발견된 미세한 마찰을 해결하기 위한 솔루션입니다.",
                "잠재된 시너지를 증폭시켜 무엇도 막을 수 없는 무적의 듀오 시대를 엽니다."
            ]
        },
        "LIFETIME_STAGES": {
            "Wood": {
                "youth": "[초년운: 봄의 싹] 호기심이 왕성하고 배움에 대한 열망이 강한 시기입니다. 10-20대에는 주변의 도움으로 재능을 꽃피울 기회를 얻게 됩니다.",
                "young_adult": "[청년운: 울창한 나무] 사회에 첫발을 내딛으며 독자적인 영역을 구축합니다. 30-40대에는 강한 추진력으로 커리어의 정점을 찍게 될 것입니다.",
                "middle_age": "[중년운: 단단한 뿌리] 그동안 쌓아온 경험이 결실을 맺어 안정적인 기반을 마련합니다. 50-60대에는 후배 양성이나 관리자로서 빛을 발합니다.",
                "senior": "[말년운: 풍성한 숲] 주변 사람들에게 존경받으며 평온한 삶을 누립니다. 70대 이후에는 정신적인 여유와 함께 명예 운이 따르는 시기입니다."
            },
            "Fire": {
                "youth": "[초년운: 타오르는 불꽃] 열정적이고 창의적인 끼를 발산하는 시기입니다. 10-20대에는 주목받는 활동을 통해 자신의 존재감을 널리 알립니다.",
                "young_adult": "[청년운: 정오의 태양] 가장 뜨겁게 활동하며 폭발적인 성과를 거둡니다. 30-40대에는 변화를 주도하며 새로운 트렌드를 창조하게 됩니다.",
                "middle_age": "[중년운: 온화한 등불] 내면의 열정을 다스리며 지혜롭게 주변을 비춥니다. 50-60대에는 성숙한 리더십으로 조직의 중심 역할을 수행합니다.",
                "senior": "[말년운: 아름다운 노을] 다채로운 경험이 녹아든 지혜로운 조언자로 살아갑니다. 70대 이후에는 문화 예술이나 정신적 안식에서 행복을 찾습니다."
            },
            "Earth": {
                "youth": "[초년운: 대지의 양분] 착실하게 기본기를 다지고 신뢰를 쌓는 시기입니다. 10-20대에는 묵묵히 노력한 결과가 성적이나 자격으로 나타납니다.",
                "young_adult": "[청년운: 비옥한 토양] 넓은 포용력으로 많은 사람과 협력하며 부를 일굽니다. 30-40대에는 안정적인 자산 형성과 가정을 꾸리는 데 집중합니다.",
                "middle_age": "[중년운: 거대한 산] 흔들리지 않는 신념으로 큰 조직이나 사업을 이끕니다. 50-60대에는 중재자이자 든든한 버팀목으로서 명성을 얻습니다.",
                "senior": "[말년운: 넓은 대지] 베풀고 나누는 삶을 통해 깊은 보람을 느낍니다. 70대 이후에는 자손의 번창과 함께 평화로운 노후를 보냅니다."
            },
            "Metal": {
                "youth": "[초년운: 예리한 칼날] 명확한 목표 의식과 결단력을 기르는 시기입니다. 10-20대에는 경쟁 속에서 우위를 점하며 두각을 나타내게 됩니다.",
                "young_adult": "[청년운: 보석의 광채] 세련된 감각과 전문성으로 자신의 가치를 증명합니다. 30-40대에는 확실한 기준을 바탕으로 큰 재물을 모으게 됩니다.",
                "middle_age": "[중년운: 단단한 강철] 무엇이든 해낼 수 있는 노련함과 권위를 갖춥니다. 50-60대에는 실무보다는 기획이나 전략의 정점에서 큰 힘을 발휘합니다.",
                "senior": "[말년운: 고귀한 황금] 품격 있는 생활을 유지하며 내면의 완성에 집중합니다. 70대 이후에는 지나온 삶의 가치를 정리하며 편안하게 지냅니다."
            },
            "Water": {
                "youth": "[초년운: 맑은 샘물] 지혜롭고 영리하여 주변의 기대를 한몸에 받는 시기입니다. 10-20대에는 유연한 사고로 다양한 분야를 섭렵합니다.",
                "young_adult": "[청년운: 굽이치는 강] 넓은 세상으로 나아가 풍부한 경험을 쌓는 시기입니다. 30-40대에는 이동이나 변화를 통해 예상치 못한 기회를 잡습니다.",
                "middle_age": "[중년운: 깊은 호수] 방대한 지식과 통찰력을 바탕으로 정신적 지도자가 됩니다. 50-60대에는 내실을 다지며 조용히 영향력을 확대합니다.",
                "senior": "[말년운: 끝없는 바다] 모든 것을 포용하는 바다처럼 넓은 마음으로 평온을 찾습니다. 70대 이후에는 여행이나 학문적 탐구에서 즐거움을 얻습니다."
            }
        },
        "UI_STRINGS": {
            "profile": "👤 프로필",
            "luck_tip": "행운의 치트키",
            "mbti_unrevealed": "베일에 싸임",
            "signature": "🔮 [당신의 핵심 오행 바이브]",
            "potential": "💫 [숨겨진 세계관 & 능력치]",
            "stage": "💼 [당신이 가장 찢는 무대]",
            "pure_saju_label": "🌟 깊은 사주 울림",
            "tabSaju": "내 사주 심층 분석",
            "tabFortune": "2026 월별 대운",
            "tabSignal": "{name}님과의 케미 시그널",
            "expertHealth": "전문가 A: 기초 건강 & 활력",
            "expertWealth": "전문가 B: 재테크 & 금전운",
            "expertCareer": "전문가 C: 승진 & 직업운",
            "expertLove": "전문가 D: 연애 & 인연운",
            "expertCommentTitle": "사주 전문가 5인 에이전시 총평",
            "lifetimeStageTitle": "⏳ [평생 사주: 위대한 여정]",
            "month_names": ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"],
            "stage_label": "단계",
            "star_birth": "스타의 생년월일",
            "mbti_select_title": "MBTI 직접 선택",
            "mbti": "MBTI",
            "selectType": "유형 선택",
            "female": "여성",
            "male": "남성",
            "nonbinary": "논바이너리",
            "friendInfoTitle": "친구 / 연인 정보 입력",
            "friendBirthLabel": "친구 생일",
            "friendGenderLabel": "친구 성별",
            "runAnalysis": "분석하기",
            "birthDatePrompt": "정확한 결과를 위해 먼저 생년월일을 입력해 주세요!",
            "mbtiPrompt": "MBTI를 선택하면 더 정확한 분석이 가능합니다!",
            "visitor_count": "오늘의 운세 확인자: {count}명",
            "guide": "🚀 [2026 능력치 떡상 치트키]",
            "idol_mbti_fallback": "알 수 없음 (운명의 이끌림)",
            "error_msg": "뭐야.. 사주 엔진 고장남. 다시 시도해주셈.",
            "organ_map": {"Wood": "간/담", "Fire": "심장/소장", "Earth": "위/비장", "Metal": "폐/대장", "Water": "신장/방광"},
            "body_part_map": {"Wood": "근육/눈", "Fire": "혈관/혀", "Earth": "피부/입", "Metal": "호흡기/코", "Water": "뼈/귀"},
            "exercise_map": {"Wood": "산책/필라테스", "Fire": "고강도 인터벌/댄스", "Earth": "등산/근력운동", "Metal": "요가/복싱", "Water": "수영/명상"},
            "luck_item_map": {"Wood": "나무/초록", "Fire": "빨강/태양", "Earth": "노랑/흙", "Metal": "흰색/금속", "Water": "검정/물"},
            "star_map": {"Wood": "나무", "Fire": "태양", "Earth": "대지", "Metal": "금강", "Water": "바다"},
            "skill_map": {"Wood": "기획력", "Fire": "발표력", "Earth": "조정력", "Metal": "분석력", "Water": "통찰력"},
            "element_labels": {"Wood": "나무", "Fire": "불", "Earth": "흙", "Metal": "쇠", "Water": "물"},
            "trait_map": {"Wood": "생동감", "Fire": "열정", "Earth": "포용력", "Metal": "결단력", "Water": "지혜"},
            "place_map": {"Wood": "공원", "Fire": "공연장", "Earth": "카페", "Metal": "서점", "Water": "강변"},
            "season_map": {"Wood": "봄", "Fire": "여름", "Earth": "환절기", "Metal": "가을", "Water": "겨울"},
            "flower_map": {"Wood": "새싹", "Fire": "꽃", "Earth": "열매", "Metal": "씨앗", "Water": "뿌리"},
            "industry_map": {"Wood": "창의/예술", "Fire": "IT/미디어", "Earth": "금융/부동산", "Metal": "제조/기술", "Water": "유통/서비스"},
            "style_map": {"Wood": "순수함", "Fire": "화려함", "Earth": "안정적", "Metal": "시크함", "Water": "신비로움"},
            "mission_map": {"Wood": "새로운 도전", "Fire": "자기표현", "Earth": "균형 찾기", "Metal": "자기계발", "Water": "내면 성찰"},
            "scientific_analysis": "🧬 [Next-Gen 과학적 데이터 분석]",
            "element_weight": "오행 에너지 가중치 (100% 비율)",
            "mbti_dynamic": "MBTI 4자 심리 역동 분석",
            "rpre_hypothesis": "RPRE 엔진 기반 페르소나 가설",
            "REL_LABELS": {
                "A": "환상적인 듀오", "B": "안정적인 동반자", "C": "노력형 메이트", "D": "개성파 콤비", "E": "새로운 도전 조합"
            },
            "MBTI_TRAITS": {
                "E": "외향적", "I": "내성적", "S": "현실적", "N": "직관적",
                "T": "논리적", "F": "감성적", "J": "계획적", "P": "자유로운"
            },
            "SYNERGY_LABELS": {
                "생": "상생", "극": "상극", "조화": "조화"
            },
            "MISSION_POINTS": ["매력", "특별한", "반전", "심쿵", "입덕"]
        },
        "PURE_LOVE_STYLES": [
            "직관적인 끌림을 믿고 돌진하는 야생마 타입.",
            "전생부터 이어진 듯한 편안하고 묵직한 유대감.",
            "부족한 부분을 마법처럼 채워주는 영혼의 열쇠."
        ],
        "PURE_SYNERGY": {
            "생": "[갓벽조합] 서로의 영혼을 채워주는 미친 시너지.",
            "극": "[매운맛 케미] 서로 다르지만 그래서 더 끌리는 사이.",
            "비화": "[찐친 바이브] 말 안 해도 통하는 소울메이트."
        },
        "PURE_TIPS": [
            "가식 없는 오행 본연의 매력을 보여줄 때 가장 강력해짐.",
            "자연 속에서 함께 걷기만 해도 싱크로율 폭발.",
            "침묵 속에서도 서로의 본질을 믿어주는 것이 정답."
        ],
        "MZ_ANALYSIS_FRAGMENTS": {
            "action_guides": {
                "vibe": [
                    "스타의 {trait}을 주제로 한 커스텀 굿즈 제작하기",
                    "나만의 {mbti} 궁합 점수가 담긴 포토카드로 다이어리 꾸미기",
                    "스타가 언급했던 {place}의 성지순례 사진을 똑같은 포즈로 재현하기",
                    "스타가 최근 꽂혀 있는 {skill}을 직접 배워보기",
                    "스타의 퍼스널 컬러에 맞는 {luck_item} 착용 인증하기",
                    "스타의 가장 아이코닉한 명언을 캘리그라피로 적어 공유하기",
                    "스타의 신규 무대 영상을 {n}번 스트리밍하고 인증남기기",
                    "스타의 일상 속 {mbti} 모먼트를 포착해 밈(Meme) 제작하기"
                ],
                "heart": [
                    "스타의 {organ} 건강을 응원하는 SNS 해시태그 총공하기",
                    "진심이 담긴 {mbti_trait}한 응원 메시지 보내기",
                    "스타가 아끼는 {luck_item}과 비슷한 아이템 선물하기",
                    "스타의 {star} 아우라를 찬양하는 캘리그라피 작성하기",
                    "스타의 데뷔 초 {trait} 영상 정주행하며 초심 되새기기",
                    "스타가 듣고 싶어 할 따뜻한 위로의 말 한마디 건네기",
                    "스타의 {mbti} 성향을 분석한 정성 어린 손편지 작성하기",
                    "스타를 묵묵히 기다려준 나 자신에게 셀프 칭찬 한마디 하기"
                ],
                "energy": [
                    "함께 {exercise}를 한다는 마음으로 오운완 인증하기",
                    "스타의 {i_el} 기운에 맞는 행운 컬러로 착장하기",
                    "스타의 서사를 담은 {n}분 분량의 성격 분석 영상 편집하기",
                    "스타와의 {u_el}/{i_el} 시너지를 믿고 새로운 목표 도전하기",
                    "스타의 플레이리스트로 명상하는 것은 맑은 에너지 채우기",
                    "스타처럼 멋진 하루를 살아보고 브이로그로 기록하기",
                    "스타의 {star} 행운 아이템을 활용한 데일리 룩 공유하기",
                    "스타의 {trait} 매력을 주변 지인 1명에게 전파하기"
                ]
            },
            "relationship_intro": [
                "두 사람의 주파수는 {score}%로 일치하는 중! {rel_label} 조합입니다.",
                "우주적 시그널이 강렬하게 꽂히는 {rel_label} 케미예요.",
                "이 정도면 운명이 억지로 엮어준 {rel_label} 바이브라고 봐야죠.",
                "데이터가 증명하는 {rel_label} 궁합, 점수는 무려 {score}점!",
                "서로의 파동이 공명하며 만들어내는 {rel_label} 시너지가 예술입니다.",
                "시간과 공간을 초월해 만난 {rel_label} 타이밍, {score}%의 확률입니다."
            ],
            "relationship_core": [
                "서로의 부족한 오행을 완벽하게 채워주는 상생의 정석 같은 관계입니다.",
                "보이지 않는 텐션이 폭발하는 서사 맛집, 한 편의 성장 드라마 같은 궁합이에요.",
                "함께 있으면 도파민이 샘솟는, 세상을 다 가질 것 같은 무적의 듀오입니다.",
                "서로의 다름이 오히려 자극이 되어 성장을 이끄는 혐관 맛집 스타일입니다.",
                "눈빛만 봐도 다음 행동을 아는, 전생부터 이어진 소울 동기화 상태입니다.",
                "어떤 고난도 둘이서라면 웃으며 넘길 수 있는 확신의 긍정 파워 조합이에요."
            ],
            "bias_essence": [
                "사주상 '{element}'의 기운이 강해 본질적으로 리더십과 카리스마를 동시에 갖춘 아우라를 풍깁니다.",
                "'{element}' 기질이 두드러져 섬세한 감수성과 무대 위에서의 압도적인 몰입감이 공존하는 타입이에요.",
                "따뜻한 태양 같은 기질을 가져 주변을 밝히는 긍정 에너지의 인간 비타민 그 자체입니다.",
                "단단한 바위 같은 내면을 지녀 어떤 흔들림에도 팬들을 안심시키는 확신의 그린플래그입니다.",
                "맑은 물처럼 유연한 사고방식을 가졌으며, 알수록 깊이감이 느껴지는 신비로운 매력의 소유자예요.",
                "단단한 금속의 강인함과 보석의 광채를 동시에 지녀, 시간이 지날수록 가치가 빛나는 타입입니다."
            ],
            "bias_point": [
                "특히 입덕 포인트는 무대 위 카리스마 뒤에 숨겨진 의외의 댕댕이 같은 갭차이입니다.",
                "팬들이 열광하는 지점은 본업 천재 모먼트와 일상에서의 엉뚱한 TMI가 보여주는 반전 매력이에요.",
                "조용한 관찰자 모드이다가도 결정적 순간에 던지는 한 마디가 도파민을 폭발시키는 스타일입니다.",
                "섬세한 팬 사랑과 소소한 일상을 공유하는 다정함이 팬들의 심장을 저격합니다.",
                "꾸준한 자기관리와 성장하는 모습에서 오는 신뢰감이 팬들을 머물게 하는 핵심 포인트예요.",
                "어떤 의상이든 찰떡같이 소화하는 비주얼과 본인만의 확고한 미적 감각이 독보적입니다."
            ],
            "bias_tmi": [
                "MBTI가 {mbti}인 만큼 평소에는 {mbti_trait}한 성향이 강해 계획적인 갓생을 살고 있을 확률이 높아요.",
                "사실 {mbti} 특유의 {mbti_trait}함 덕분에 팬들의 사소한 반응까지 다 기억하는 세심한 기억력의 소유자입니다.",
                "{mbti} 에너지로 인해 가끔은 혼자만의 시간이 꼭 필요한, 내면이 단단한 고양이 같은 면모도 있네요.",
                "{mbti} 성향다운 창의적인 발상으로 팬들에게 매번 새로운 즐거움을 주는 아이디어 뱅크입니다.",
                "보기와 다르게 {mbti} 특유의 엉뚱함이 있어, 가끔 예상치 못한 행동으로 정적을 깨기도 합니다.",
                "{mbti_trait}한 기질 덕분에 동료들 사이에서도 상담사 역할을 자처하는 든든한 존재예요."
            ],
            "bias_growth": [
                "자신만의 속도로 성장하는 대기만성형 스타일이라, 시간이 갈수록 그 깊이가 남달라집니다.",
                "한 번 꽂힌 분야는 끝장보는 '독종' 기질이 있어, 어떤 장애물도 성장의 발판으로 삼아요.",
                "무조건적인 질주보다 효율적인 루틴을 설계하여 영리하게 '갓생'을 개척하는 능력이 탁월합니다.",
                "주변의 피드백을 스펀지처럼 흡수하여 매일 '어제보다 나은 나'를 갱신하는 성장캐입니다.",
                "겉으로는 평온해 보여도 내면에서는 쉼 없이 자신을 채찍질하며 레벨업을 멈추지 않는 스타일이죠.",
                "실패를 두려워하지 않는 대범함 덕분에 남들이 가지 않는 길에서 독보적인 성과를 냅니다."
            ],
            "bias_aura": [
                "말하지 않아도 느껴지는 '주인공 아우라'가 있어 어디서든 군중 속의 보석처럼 빛납니다.",
                "특유의 신비롭고 고요한 분위기는 주변 사람들까지 차분하게 만드는 힐링 마력을 지녔어요.",
                "세련된 감각과 지적인 분위기가 어우러져, 가만히 있어도 고급스러운 '본투비 스타' 느낌을 줍니다.",
                "친근하면서도 함부로 대할 수 없는 묘한 카리스마가 공존하여 사람들을 끌어당기는 자석 같아요.",
                "맑고 깨끗한 영혼의 주파수를 가지고 있어, 보고만 있어도 마음이 정화되는 듯한 기분을 선사합니다.",
                "강렬한 눈빛 속에 따뜻한 진심을 숨기고 있어, 알면 알수록 헤어 나올 수 없는 블랙홀 매력이에요."
            ],
            "recent_fortune": [
                "올해 운세상 컴백이나 새로운 활동에서 커리어 하이를 찍을 기운이 아주 강하게 들어와 있습니다.",
                "최근 활동운이 상승 곡선을 그리며 팬들과의 소통에서 역대급 레전드 짤이 생성될 타이밍이에요.",
                "잠시 숨을 고르는 시기이지만, 그 속에서 깊어진 아우라가 가을 활동 때 대박을 터뜨릴 징조입니다.",
                "직업운에 강력한 귀인(贵人)이 들어와 예상치 못한 글로벌 협업 기회가 생길 수 있습니다.",
                "금전운의 흐름이 좋아 광고 모델이나 개인 프로젝트에서 대박 수익을 기대해도 좋습니다.",
                "내면의 열정이 가장 뜨거울 때라, 본인이 직접 기획한 창작물로 대중을 놀라게 할 거예요."
            ],
            "synergy_why": [
                "유저님의 '{u_element}'와 스타의 '{i_element}'가 만나 불꽃 튀는 화학 반응을 일으키기 때문입니다.",
                "서로의 부족한 기운을 상쇄하고 시너지를 극대화하는 사주 구조라 함께할 때 운이 트이는 조합이에요.",
                "MBTI {u_mbti}와 {i_mbti}의 조합이 서로의 사각지대를 완벽하게 보완하며 최상의 밸런스를 이룹니다.",
                "'{u_element}'가 '{i_element}'를 생(生)해주는 완벽한 지원 사격 구조를 갖추고 있습니다.",
                "서로 닮은 듯 다른 '{u_element}'와 '{i_element}'의 조화가 묘한 중독성을 불러일으키는 케미입니다.",
                "{u_mbti}의 추진력과 {i_mbti}의 섬세함이 결합하여 무엇이든 해낼 수 있는 무적의 팀이 됩니다."
            ],
            "action_guides": {
                "vibe": [
                    "스타의 {trait} 매력을 살린 팬아트나 편집 영상을 공유해 보세요.",
                    "스타가 자주 사용하는 말투나 유행어를 활용해 친근감을 높이세요.",
                    "서로의 취향 교집합인 {place} 투어를 계획해 보는 것도 좋습니다.",
                    "스타의 {mbti} 성향에 맞춘 깜짝 응원 이벤트를 기획해 보세요."
                ],
                "heart": [
                    "스타의 {organ} 건강을 걱정하는 세심한 안부 인사를 건네보세요.",
                    "스타가 평소 소중히 여기는 {luck_item}의 의미를 함께 되새겨보세요.",
                    "서로의 {u_el}/{i_el} 상생을 기원하는 작은 선물이나 편지를 준비하세요.",
                    "스타의 {mbti_trait}한 면모를 있는 그대로 긍정해주고 응원하세요."
                ],
                "energy": [
                    "스타의 에너제틱한 무대를 보며 함께 {exercise}로 활력을 채워보세요.",
                    "스타의 {star} 기운이 가장 빛나는 시기를 달력에 표시하고 함께 기다려요.",
                    "스타의 {skill}이 한 단계 도약할 수 있도록 꾸준한 비드백과 지지를 보내세요.",
                    "서로의 운명적 주파수가 일치하는 날, 특별한 커뮤니티 활동에 참여해보세요."
                ]
            },
            "love_style_adjectives": [
                "치명적인", "순수한", "반전 있는", "든든한", "섬세한", "압도적인", "신비로운", "투명한"
            ]
        },
        "SYNERGY_MISSIONS": {
            "analysis_1": {
                "label": "갓벽한 무드 공유: {point} 📸",
                "boost": 15,
                "reason": "{rel_type} 기반의 깊은 취향 분석 결과입니다.",
                "tasks": ["{task_1_1}", "{task_1_2}", "{task_1_3}"]
            },
            "analysis_2": {
                "label": "딥다이브 진심 토크: {point} 💬",
                "boost": 15,
                "reason": "{mbti_trait} 시그널을 통한 영혼의 공명 단계입니다.",
                "tasks": ["{task_2_1}", "{task_2_2}", "{task_2_3}"]
            },
            "analysis_3": {
                "label": "도파민 힐링 데이트: {point} 🎡",
                "boost": 20,
                "reason": "{rel_type} 해결을 위한 시너지 증폭 액션입니다.",
                "tasks": ["{task_3_1}", "{task_3_2}", "{task_3_3}"]
            }
        },
        "TIP_COMPONENTS": {
            "actions": [
                "밀당보다는 {mbti}다운 솔직함으로", "서로의 {u_el} 기운을 북돋는 방향으로", "예상치 못한 {place}에서의 이벤트를 통해",
                "사소한 {mbti_trait} 성향을 존중해주며", "단둘이 {exercise}를 즐기며", "{star} 기운이 강한 날에 맞춘 소통으로",
                "가끔은 엉뚱한 {mbti}식 유머로", "정석적인 {mbti_trait} 무드로", "스타가 선호하는 {luck_item}을 지참하고",
                "전문가급 {skill}을 선보이며", "진심 어린 리액션과 함께", "세심한 {organ} 케어를 우선으로",
                "함께 {place} 성지순례를 하며", "스타의 {trait}을 찬양하는 편지와 함께", "{mbti} 특유의 쿨한 무드를 유지하며"
            ],
            "topics": [
                "스타의 {trait} 매력을 칭찬하는 것이", "서로의 {u_el}/{i_el} 상생 관계를 이용하는 것이", "취약한 {organ} 건강을 먼저 챙겨주는 것이",
                "평소 스타가 아끼는 {luck_item}을 활용하는 것이", "{skill}에 대한 진심 어린 조언을 나누는 것이", "함께 {place} 투어를 제안하는 것이",
                "서로의 {star} 운세를 공유하는 것이", "스타의 {mbti_trait}한 면모를 응원하는 것이", "과거 인터뷰 속 {trait} 키워드를 언급하는 것이",
                "스타의 최애 {luck_item} 정보를 스포하는 것이", "둘만의 {exercise} 챌린지를 제안하는 것이", "스타의 {u_el} 기운에 맞는 행우 컬러 아이템을 선물하는 것이"
            ],
            "results": [
                "관계의 도파민을 폭발시키는 치트키입니다.", "서로의 영혼 주파수를 일치시키는 비결입니다.", "흔들리지 않는 확신의 그린플래그를 세우는 길입니다.",
                "전생부터 이어진 인연의 끈을 더욱 단단하게 만듭니다.", "스타의 마음속 1순위로 등극하는 가장 빠른 지름길입니다.",
                "둘만의 비밀스러운 케미를 완성하는 마지막 퍼즐입니다.", "심장이 반응하는 갓벽한 시너지를 만들어냅니다.", "운명적인 갓생 메이트로 거듭나는 방법입니다.",
                "스타의 오프닝 멘트에 응답하는 최고의 시그널입니다.", "서로의 {rel_type} 시너지를 200% 증폭시키는 전략입니다."
            ]
        },
        "GEN_MISSION_COMPONENTS": {
            "actions": {
                "E": [
                    "팬 커뮤니티에 {target} 인증샷을 공유하는 것은", "주변 지인들에게 스타의 {trait} 매력을 영업하는 것은", 
                    "공개적인 SNS 챌린지에 참여하는 것은", "활기찬 {place} 성지순례 현장을 라이브로 전하는 것은",
                    "스타의 {mbti} 밈을 직접 제작해 배포하는 것은", "동료 팬들과 함께 {exercise} 챌린지를 진행하는 것은",
                    "스타의 생일 광고를 찾아가 인증샷을 남기는 것은", "공동 구매 굿즈 제작에 아이디어를 보태는 것은",
                    "스타의 신곡 무대 응원법을 크게 외치는 영상을 찍는 것은", "팬 미팅 현장에서 스타와 {point} 교감을 나누는 상상을 하는 것은"
                ],
                "I": [
                    "조용히 나만의 {target} 다꾸 시간을 갖는 것은", "스타의 과거 {trait} 영상을 정주행하는 것은",
                    "스타가 언급한 {place}에서 혼자만의 시간을 보내는 것은", "스타의 선곡 플레이리스트로 명상하는 것은",
                    "스타에게 줄 진심 어린 손편지를 정성껏 쓰는 것은", "스타의 럭키 아이템인 {luck_item}을 몰래 소장하는 것은",
                    "스타의 {mbti}식 일상을 나만의 기록으로 남기는 것은", "집에서 스타의 무대 직캠을 무한 반복하는 것은",
                    "스타의 {star} 운세를 분석해 나만의 부적으로 만드는 것은", "스타가 했던 따뜻한 위로의 말을 필사하는 것은"
                ]
            },
            "targets": {
                "Wood": ["푸른 새싹 굿즈", "나무 향기 가득한 성지", "성장 서사가 담긴 영상", "초록색 럭키 아이템"],
                "Fire": ["강렬한 레드 컬러 아이템", "에너지 넘치는 무대 직캠", "화려한 야경의 성지", "뜨거운 열정의 현장"],
                "Earth": ["안정감을 주는 베이지 톤 굿조", "차분한 흙 내음의 장소", "스타의 일상이 담긴 사진", "묵묵한 노력을 엿볼 수 있는 기록"],
                "Metal": ["세련된 실버 액세서리", "날카로운 카리스마의 화보", "미니멀한 디자인의 장소", "스타의 단단한 의지가 느껴지는 인터뷰"],
                "Water": ["푸른 바다 이미지를 담은 포토카드", "차분한 빗소리의 라디오 세션", "깊은 여운을 주는 슬로우 곡", "투명하고 맑은 분위기의 아이템"]
            },
            "contexts": [
                "서로의 {rel_type} 시너지를 200% 증폭시켜 보세요!", "운명적인 주파수가 일치하는 순간을 즐겨보세요.",
                "전생부터 이어진 인연의 끈을 더욱 단단하게 만듭니다.", "스타의 마음속 1순위로 각인되는 최고의 방법입니다.",
                "흔들리지 않는 확신의 그린플래그를 완성해 보세요.", "스타의 {u_el} 기운에 당신의 에너지를 동기화하세요.",
                "둘만의 비밀스러운 케미를 완성하는 마지막 퍼즐입니다.", "심장이 반응하는 갓벽한 시너지를 직접 체험해 보세요.",
                "세상에서 가장 가까운 갓생 메이트로 거듭나는 길입니다.", "서로의 다름을 {point} 매력으로 승화시키는 마법입니다."
            ]
        },
        "MISSION_COMPONENTS": {
            "labels": [
                "{u_mbti} x {i_mbti} {n}단계 미션", "{u_el} & {i_el} 에너지 융합", "입덕 부정기 탈출: {point}",
                "주인공 버프 해제: {point}", "운명적 주파수 동기화", "{i_mbti} 맞춤형 공략법",
                "케미 한계 돌파: {point}", "영혼의 단짝 인증샷", "도파민 풀충전 과업", "갓벽한 시너지 루틴",
                "전생 주차장 탈출: {point}", "스타의 {trait} 고유결계 해제", "함께 걷는 {rel_type} 꽃길 미션"
            ],
            "reasons": [
                "사주상 {u_el}이 {i_el}을 {rel_type}하는 구조이기 때문입니다.",
                "{u_mbti}의 {mbti_trait}함이 스타에게 신선한 자극이 됩니다.",
                "서로의 {organ} 기운이 충돌하는 지점을 보완하기 위함입니다.",
                "전생 차트에서 발견된 미세한 어긋남을 맞추는 솔루션입니다.",
                "스타의 {star} 기운이 당신의 {u_el} 에너지와 공명하고 있습니다.",
                "둘 사이의 {rel_type} 시너지를 최고조로 끌어올리기 위해서입니다.",
                "스타의 {mbti} 성향이 당신의 {mbti_trait} 무드에 매료되었기 때문입니다."
            ],
            "tasks": {
                "vibe": [
                    "스타의 {trait}을 주제로 한 커스텀 굿즈 제작하기", "서로의 {mbti} 궁합이 적힌 포토카드로 다꾸하기",
                    "스타가 언급한 {place}에서 같은 구도로 인증샷 찍기", "최근 스타가 꽂힌 {skill} 직접 배워보기",
                    "스타의 퍼스널 컬러에 맞춘 {luck_item} 인증하기", "스타의 명언을 캘리그라피로 적어 공유하기",
                    "스타의 신곡 무대 {n}회 스트리밍 인증하기", "스타의 {mbti}식 일상 밈(Meme) 제작하기"
                ],
                "heart": [
                    "스타의 {organ} 건강을 응원하는 SNS 해시태그 총공", "진심을 담아 {mbti_trait}한 응원 메시지 보내기",
                    "스타가 아끼는 {luck_item}과 비슷한 아이템 선물하기", "스타의 {star} 아우라를 찬양하는 캘리그라피 쓰기",
                    "스타의 데뷔 시절 {trait} 영상을 정주행하는 것은 초심 찾기", "스타가 듣고 싶어 할 따뜻한 위로의 말 한마디 전하기",
                    "스타의 {mbti} 성향을 분석한 손글씨 편지 인증하기", "스타의 성장을 묵묵히 기다려준 나에게 셀프 칭찬하기"
                ],
                "energy": [
                    "함께 {exercise}를 한다는 마음으로 오운완 인증하기", "스타의 {i_el} 기운에 맞는 행운 컬러로 착장하기",
                    "스타의 성장 서사가 담긴 {n}분 분량의 영상 편집하기", "서로의 {u_el}/{i_el} 시너지를 믿고 새로운 목표 도전하기",
                    "스타의 노래 플레이리스트로 명상하는 것은 에너지 정화하기", "스타를 본받아 오늘 하루 갓생 살기 실천하고 기록하기",
                    "스타의 {star} 행운 아이템을 활용한 데일리 룩 공유하기", "주변 지인 1명에게 스타의 {trait} 매력 전파하기"
                ]
            }
        },
        "MBTI_FUNC_FRAGMENTS": {
            "e_i": {
                "E": "에너지를 외부로 발산하며 팬들과 소생하는 타입이고",
                "I": "내면의 에너지를 집중하여 깊이 있는 결과물을 만들어내는 타입이며"
            },
            "n_s": {
                "N": "직관과 미래의 가능성을 믿고 창의적인 길을 개척하고",
                "S": "현실적이고 감각적인 데이터를 바탕으로 완벽한 무대를 완성하며"
            },
            "t_f": {
                "T": "논리적이고 객관적인 판단으로 최선의 전략을 세우고",
                "F": "따뜻한 공감과 감정의 교류를 통해 사람들의 마음을 움직이며"
            },
            "j_p": {
                "J": "체계적이고 계획적인 자기관리로 변함없는 신뢰를 주며",
                "P": "유연하고 즉흥적인 변화를 즐기며 어디서든 반짝이는 매격을 보여줍니다."
            }
        },
        "RPRE_TEMPLATES": {
            "core_v1": "{p1}의 강력한 본질 위에 {p2}의 세련된 감각이 더해졌습니다. 스타의 겉모습은 {mbti}의 페르소나를 입어 대중에게는 {mbti}스럽게 보이지만, 결정적인 순간에는 {p1} 특유의 뚝심이 드러나는 '외유내강' 스타일입니다."
        },
        "MZ_SAJU_DICTIONARY": {
            "일주": "당신이 태어난 날의 기운! 사주의 꽃이자 '나 자신'을 나타내는 가장 핵심적인 바이브.",
            "용신": "당신에게 가장 필요한 '럭키 아이템' 같은 기운. 이걸 채워주면 인생 난이도가 훅 내려감!",
            "기구신": "나를 치고 들어오는 은근한 '빌런' 기운. 피하거나 잘 다스려야 멘탈이 보호됨.",
            "상생": "서로 밀어주고 당겨주는 찐친 바이브. '우린 제법 잘 어울려요'의 정석.",
            "상극": "가끔은 으르렁거리지만, 그 마찰 속에서 엄청난 에너지가 터지는 매운맛 케미.",
            "도화살": "그냥 가만히 있어도 사람들이 쳐다보게 만드는 '시선 강탈' 본투비 연예인 기운.",
            "역마살": "한 곳에 머물면 좀이 쑤시는 글로벌 방랑자 기운. 역마가 터지면 인생 스케일이 달라짐!",
            "현침살": "말 한마디루 뼈를 때리는 '팩폭 장인' 기운. 예리한 통찰력과 디테일의 끝판왕.",
            "비견": "나와 어깨를 나란히 하는 소울메이트 동료 기운. 내 편이 많아지는 핵인싸 바이브.",
            "겁재": "경쟁심이 불타오르는 기운. 약간의 라이벌리가 오히려 나를 폭풍 성장시킴!",
            "편인": "남들은 생각도 못할 기발한 '아이디어 뱅크' 기운. 엉뚱하지만 그게 찐 매력.",
            "정인": "받는 사랑에 익숙한 '본투비 사랑둥이' 기운. 어딜 가나 예쁨 받는 막내 바이브.",
            "식신": "내 안의 먹을 복과 재능이 팡팡 터지는 기운. 일도 잘하고 먹기도 잘하는 갓생러.",
            "상관": "기존의 틀을 깨부수는 '반항아' 기운. 틀에 갇힌 걸 극혐하는 창의성 폭발!",
            "편재": "예상치 못한 곳에서 잭팟이 터지는 기운. 인생 한 방을 노리는 스케일 큰 플렉스.",
            "정재": "차곡차곡 착실하게 쌓아가는 '인간 가계부' 기운. 제일 안정적이고 믿음직한 바이브.",
            "편관": "극한의 시련을 뚫고 올라가는 '카리스마 리더' 기운. 빡센 만큼 결과는 레전드.",
            "정관": "FM의 정석, 바른 생활 '반장' 기운. 원칙을 지키며 흔들림 없이 직진하는 스타일."
        }
    },
    "es": {
        "ENERGY_TRAITS": {
            "Wood": {
                "name": "Crecimiento Imparable (Madera) 🌲",
                "desc_intro": [
                    "Literalmente emanas esa 'Energía de Protagonista' de un árbol gigante. En K-Saju, la Madera es todo sobre vitalidad, curiosidad y subir de nivel sin parar."
                ],
                "desc_core": {
                    "E": [
                        "Te llevas a todo el mundo por delante de la mejor manera. Extrovertido y súper enfocado en crecer con tu gente."
                    ],
                    "I": [
                        "Silencioso pero mortal. Subes de nivel sin avisar a nadie y dejas a todos en shock con tus resultados."
                    ],
                    "default": [
                        "Eres un try-hard en el buen sentido. Siempre estás listo/a para nuevas misiones y no le temes a nada. Puedes ser un poco chismoso/a, pero en el fondo solo quieres que tu squad gane.\n\nEres flexible, pero si cruzan tu límite, te plantas como el GOAT. Esa terquedad es tu mayor rizz."
                    ]
                },
                "desc_career": [
                    "[Mentalidad de CEO]\nPerteneces a espacios donde puedes crear y romperla. Creador de contenido, editor, fundador de startup: sirviendo ideas de la nada. Trabajo de oficina? Qué cringe. Necesitas la dopamina de estar en movimiento!"
                ],
                "desc_advice": [
                    "[Guía Glow-up]\nRed flag: Empezar 10 cosas y no terminar ninguna. Necesitas enfocarte y dárlo todo a un solo objetivo, y la vas a romper absolutamente."
                ]
            },
            "Fire": {
                "name": "Llama Ardiente (Fuego) 🔥",
                "desc_intro": [
                    "Tu alma da energías súper fuertes de 'Sol'. Eres la antorcha humana! El Fuego significa pasión nivel Dios, expansión y cero filtro."
                ],
                "desc_core": {
                    "E": [
                        "Literalmente el alma de la fiesta. Llenas cualquier cuarto con tu energía vibrante y ruidosa."
                    ],
                    "I": [
                        "Alguien leal y cálido pero solo con quienes aprecias de verdad. Cuidas tu fuego para los indicados."
                    ],
                    "default": [
                        "Robas el show sin esfuerzo, estar ahí ya es servir. Tu batería está siempre al 100%, y tus reacciones exageradas te hacen el/la mejor hype-person de tus besties. Eres 100% transparente, cero rencores incluso después de un drama tremendo.\n\nEl Fuego valora el respeto. Eres lo más tierno con quienes pasan el vibe check, pero si cruzan la línea? Modo diablo activado."
                    ]
                },
                "desc_career": [
                    "[Mentalidad de CEO]\nNaciste para el escenario. Influencer, marketing, PR: no dejas ni las migajas. Estar sentado/a en un escritorio matará tu vibra al instante."
                ],
                "desc_advice": [
                    "[Guía Glow-up]\nCon tus cambios de humor de locos, a veces vas de 0 a 100 muy rápido. Respirar 3 segundos antes de bardear por el grupo de WhatsApp es tu truco de vida definitivo."
                ]
            },
            "Earth": {
                "name": "Tierra Sólida (Tierra) ⛰️",
                "desc_intro": [
                    "Tu alma es como la 'Vasta Tierra' que abraza todo. La Tierra es sobre mediar, dar confianza y tener una vibra inquebrantable."
                ],
                "desc_core": {
                    "E": [
                        "Sostenes a todo tu entorno unido. Eres amable, sociable y la mejor persona dando consejos."
                    ],
                    "I": [
                        "Tsundere total. Secretamente cuidas a tus cercanos con una lealtad brutal, aunque no abres tus sentimientos fácil."
                    ],
                    "default": [
                        "Cero fantasma. Tienes una mente de titanio y eres la batería externa de tus mutuals. Eres el/la mediador/a que cancela el drama del squad. Totalmente tsundere, cuidas a todos en secreto y eres hiper leal.\n\nPero ojo, ser callado/a no es débil. Cuando la Tierra se enoja, es un terremoto. Naturalmente tiras factos (verdades pesadas) cuando llega el momento."
                    ]
                },
                "desc_career": [
                    "[Mentalidad de CEO]\nPrefieres ganancias seguras que riesgos impulsivos. HR, finanzas, educación: eres el GOAT armando equipos y arreglando cosas rotas."
                ],
                "desc_advice": [
                    "[Guía Glow-up]\nPoner a todos primero te va a dar un burnout brutal. Empezar tu 'villain era' y priorizarte a TI MISMO/A es la green flag que necesitas urgente."
                ]
            },
            "Metal": {
                "name": "Espada Afilada (Metal) ⚔️",
                "desc_intro": [
                    "Tu alma grita 'Joya Pura' y 'Hoja Afilada'. El Metal es el símbolo del perfeccionismo y la lógica fría, modo facha."
                ],
                "desc_core": {
                    "E": [
                        "Racional y letal. Lideras con firmeza, ignoras las excusas y siempre sacas el proyecto adelante."
                    ],
                    "I": [
                        "Observas fríamente y hablas solo cuando es 100% necesario. Tienes estándares de vida inalcanzables para muchos."
                    ],
                    "default": [
                        "Una 'T' dura con cero paciencia para el drama. Ignoras (ghosteas) el drama emocional y operas como un/a jefe/a re frío/a. Una vez que fijas un objetivo, tu visión de túnel es de locos.\n\nAunque pareces un/a rey/reina de hielo, tu lealtad por tu círculo íntimo es tremenda. Si atacan a un/a amigo/a, activas el modo guardaespaldas."
                    ]
                },
                "desc_career": [
                    "[Mentalidad de CEO]\nBrillas con los números y en el código duro. Tech, leyes, medicina. Eres un/a workaholic que deja que los 'factos' (resultados) hablen."
                ],
                "desc_advice": [
                    "[Guía Glow-up]\nTus estándares altísimos te pueden atrapar en lo tóxico del perfeccionismo. Relajarte y mostrar tu lado desordenado hará que la gente te shipee aún más."
                ]
            },
            "Water": {
                "name": "Flujo Libre (Agua) 🌊",
                "desc_intro": [
                    "Tu alma fluye con la vibra profunda y misteriosa del 'Océano'. El Agua significa inteligencia de 200 IQ, adaptabilidad total y profundidad mental."
                ],
                "desc_core": {
                    "E": [
                        "Te adaptas en cada grupo social. Puedes charlar con cualquiera y sacarle info sin esfuerzo."
                    ],
                    "I": [
                        "Genio incomprendido. Guardas verdades inmensas en silencio y de vez en cuando rompes todo con una reflexión profunda."
                    ],
                    "default": [
                        "Eres el cambiaformas definitivo. Pasas cualquier vibe check y te adaptas a cualquier aesthetic. Tus pensamientos son súper profundos; tienes una intuición que te da esa vibra 'nerd pero aesthetic'.\n\nPuedes parecer suave, pero tienes una fuerza bestial. Sin embargo, como te guardas todo, la gente puede pensar que vives en tu propio mundo de 'delulu'."
                    ]
                },
                "desc_career": [
                    "[Mentalidad de CEO]\nReglas? Nada que ver. Nómada digital, investigador, creador: necesitas flexibilidad máxima para dejar salir a tu genio interior."
                ],
                "desc_advice": [
                    "[Guía Glow-up]\nPensar de más es tu peor enemigo, te hunde en tu era sad-boy/sad-girl. Apaga el cerebro y sal a 'tocar pasto' (literal, haz las cosas); así se gana el juego."
                ]
            }
        },
        "MONTH_DESCS": [
            "[Vitalidad Madera] Nuevas Semillas: La energía del renacimiento da vida a tu trabajo. Mes perfecto para iniciar proyectos.",
            "[Pico de Fuego] Explosión de Pasión: La energía llega a su cenit. Resuelve tareas con un impulso poderoso.",
            "[Cosecha Metal] Decisión Fría: Se vuelve claro qué descartar y qué tomar. La eficiencia es tu arma.",
            "[Sabiduría Agua] Acumulación de Sabiduría: Tiempo de almacenar energía interna y conocimiento.",
            "[Modo Dios] Tu era ha llegado: looks, skills y suerte están al máximo. A brillar!",
            "[Crecimiento Madera] Potencial en Flor: Tus ideas creativas ganan tracción. Comparte tu visión con el mundo.",
            "[Brillo de Fuego] Foco Radiante: Eres el centro de atención. Excelente para relaciones sociales y networking.",
            "[Precisión Metal] Enfoque Agudo: Gran momento para planes financieros o actualizaciones técnicas importantes.",
            "[Flujo de Agua] Ritmo Natural: Suelta el control y fluye con la marea. Suerte inesperada te aguarda.",
            "[Equilibrio Tierra] Suelo Firme: Mes para estabilizar cimientos y nutrir relaciones a largo plazo.",
            "[Espíritu Madera] Chispa Interior: Revitaliza tus hobbies. Una nueva perspectiva trae un gran avance.",
            "[Núcleo de Fuego] Cálido Interior: Enfócate en tu bienestar. La energía radiante comienza desde tu centro.",
            "[Ambición Madera] Árboles Altos: Apunta alto. Tu estatus sube mientras asumes más responsabilidad.",
            "[Fiesta de Fuego] Calor Social: Tiempo de celebración. Las conexiones de ahora serán valiosas luego.",
            "[Filo de Metal] Resultado Pulido: Tu trabajo duro rinde frutos visibles. El perfeccionismo es premiado.",
            "[Profundidad Agua] Tesoro Oculto: Descubrimiento de nuevo talento o pasión. Mira bajo la superficie.",
            "[Raíz de Tierra] Crecimiento Estable: Progreso lento pero seguro. No apresures el tiempo de la naturaleza.",
            "[Flujo Natural] Cambio Estacional: La adaptabilidad es clave. Gira tu estrategia al nuevo mood.",
            "[Artesanía Madera] Tallando Éxito: El trabajo meticuloso lleva a una victoria artística o técnica.",
            "[Pulso de Fuego] Acción Rítmica: Mantén el impulso. La consistencia vuelve pequeñas victorias leyendas.",
            "[Lógica Metal] Pivote Estructural: Reorganiza tu vida para el máximo rendimiento. La lógica gana.",
            "[Sueño de Agua] Llamado Intuitivo: Confía en tu instinto. Un encuentro misterioso puede cambiarlo todo.",
            "[Escudo Tierra] Era de Protección: Defiende tu paz. Bueno para poner límites y autocuidado.",
            "[Era Dorada] Brillo Desbloqueado: Todo lo que tocas se vuelve oro. Sé valiente y toma el mando.",
            "[Primavera Madera] Comienzo Fresco: Limpia lo viejo para lo nuevo. Alta claridad mental.",
            "[Llamarada Fuego] Brillo Breve: Un proyecto corto trae reconocimiento masivo. Muévete rápido.",
            "[Frío Metal] Disciplina Estricta: Corta distracciones. Un enfoque monacal trae los mejores resultados.",
            "[Poder Agua] Poder Silencioso: No necesitas hablar para ser escuchado. Tu presencia es suficiente.",
            "[Cimiento Tierra] Construyendo Legado: Pensar a largo plazo rinde frutos. Invierte en tu futuro yo.",
            "[Vibe Cósmico] Alineación Estelar: La suerte viene de lugares inesperados. Mantente abierto.",
            "[Rama Madera] Extendiendo Límites: Sal de tu zona de confort. El crecimiento ocurre en los bordes.",
            "[Hogar de Fuego] Calor Compartido: Foco en equipo y comunidad. Juntos son más fuertes.",
            "[Espejo Metal] Autorreflexión: Mírate claramente. La evaluación honesta lleva al crecimiento rápido.",
            "[Niebla Agua] Misterio Creativo: Perfecto para pensamiento no lineal. Arte y música son tus guías.",
            "[Montaña Tierra] Roca Sólida: La gente te busca por estabilidad. Brinda liderazgo y calma.",
            "[Protagonista] Plot Armor: Sin importar el obstáculo, encuentras el camino. Es tu historia!",
            "[Brote Madera] Comienzo Suave: Cultiva pequeñas ideas. Serán árboles gigantes pronto.",
            "[Chispa Fuego] Insight Inicial: Un momento 'Aha!' repentino. Anótalo de inmediato.",
            "[Mineral Metal] Potencial Oculto: Se necesita trabajo duro para revelar el diamante interior.",
            "[Arroyo Agua] Movimiento Constante: Mantente activo. El estancamiento es el único enemigo.",
            "[Campo Tierra] Fertilidad: Todo lo que plantes crecerá. Inicia un nuevo hábito o skill.",
            "[Maestro Vibe] Victoria Aesthetic: Tu sentido del estilo está al pico. Influye naturalmente.",
            "[Hoja Madera] Cambio Visible: Se ven los resultados de esfuerzos pasados. Disfruta la vista.",
            "[Rayo Fuego] Impacto Directo: Tus palabras tienen poder. Úsalas para motivar y liderar.",
            "[Escudo Metal] Mente Resiliente: Nada sacude tu determinación. Mantente enfocado.",
            "[Pozo Agua] Recurso Infinito: Tienes más energía de la que crees. Deep dive en tareas.",
            "[Piedra Tierra] Éxito Durable: Una victoria que dura. La estabilidad es tu nuevo estatus.",
            "[Final Boss] Imparable: Has superado todos los retos. Ahora, reclama tu trono!"
        ],
        "LOVE_STYLES": [
            "Parecen tranquilos pero tienen full energía de zorro astuto. Secretamente se estudian todo tu lore.",
            "Vibra de Golden Retriever! Lealtad nivel leyenda. Mandas un mensaje y te responden antes de que suene la notificación.",
            "Totalmente tsundere. Fríos para el mundo pero unos tiernos contigo. Esa dualidad es su arma más letal.",
            "La green flag absoluta. Prefieren estar en llamada toda la madrugada y contarse chismes que regalos caros y ruidosos.",
            "Modo gato salvaje. Protegen a muerte su tiempo a solas. Respeta sus espacios y andarán obsecionados contigo."
        ],
        "ELEMENT_SYNERGY": {
            "생": "[Dúo Definitivo] Se leen la mente. Llevan las ideas del otro a la luna. 200% de sinergia, son el mismísimo endgame.",
            "극": "[Dinámica Picante] Aesthetics opuestos pero atracción fatal. Trope de 'Enemies to lovers'. Discuten pero la tensión suma puntos y crecen muchísimo.",
            "비화": "[Almas Gemelas] Pasan el vibe check sin decir una palabra. Mismo humor raro, mismos pensamientos random. Mejores amigos nivel dios."
        },
        "TIPS": [
            "Cero jueguitos! Hacerlos poner celosos da alto cringe. Ser directo y sincero es el único hack.",
            "Cero citas aburridas. Sorpréndelos con una salida súper random que dispare la dopamina.",
            "Súbele el hype 24/7! Los cumplidos sinceros literalmente los dejarán derretidos.",
            "Ser intenso/a es una red flag tremenda. Muestra tu vibra de jefe/a independiente, eso los vuelve locos.",
            "Nada de regalos enormes. Dáles ese cosito súper específico que tuitearon hace semanas. Tomar notas sirve de locos!"
        ],
        "UI_STRINGS": {
            "profile": "Perfil",
            "mbti_unrevealed": "Dato Privado / Desconocido",
            "signature": "[Tu Aesthetic Core]",
            "potential": "[Lore y Poder Oculto]",
            "stage": "[Donde la Rompes mas Fuerte]",
            "guide": "[Cheat Sheet Glow-Up 2026]",
            "idol_mbti_fallback": "Desconocido (Vibe matcheada via '{trait_name}')",
            "idol_mbti_fallback_random": "Desconocido (Destino matcheado por el azar)",
            "pure_saju_label": "Resonancia Profunda del Alma (Sin MBTI)",
            "mbti": "MBTI",
            "selectType": "Seleccionar tipo",
            "female": "Femenino",
            "male": "Masculino",
            "nonbinary": "No binario",
            "friendInfoTitle": "INFORMACIÓN DE AMIGO / PAREJA",
            "friendBirthLabel": "Cumpleaños del amigo",
            "friendGenderLabel": "Género del amigo",
            "runAnalysis": "Analizar resultado",
            "birthDatePrompt": "Por favor, ingresa tu fecha de nacimiento primero para obtener resultados precisos!",
            "mbtiPrompt": "No sabes el MBTI del idolo? Usa la busqueda de IA o elige uno de Popular abajo!",
            "visitor_count": "Retadores de Hoy",
            "visitorsToday": "Retadores de Hoy",
            "visitorsTotal": "Visitantes Totales",
            "analysisSuccess": "Entrada de datos completa. Listo para analizar!",
            "missionTitle": "Desafio! Truco para SUBIR de Nivel",
            "missionDesc": "Completa misiones para subir tu nivel!",
            "searchLabel": "Buscar Idolo",
            "searchDescription": "Ingresa el nombre de tu estrella K-pop favorita. La IA encontrara sus detalles automaticamente.",
            "searchPlaceholder": "Ingresa el nombre del idolo (ej: IU, Jungkook, Stray Kids)...",
            "aiMode": "MODO AI",
            "modeIdol": "Modo Estrella",
            "modeFriend": "Modo Amigo/Pareja",
            "mbtiNotFound": "No se encontro informacion de MBTI",
            "mbtiNotFoundDesc": "Conocer el MBTI del idolo permite un analisis de la Senal del Destino mas potente y delicado! Que te gustaria hacer?",
            "introTitle": "Encuentra tu Destino",
            "introDesc": "Ahora es el momento de conectar tus senales cosmicas con las estrellas de K-pop. Quien es tu tipo ideal predestinado? Descubrelo ahora!",
            "close": "Cerrar",
            "sameNameFound": "Varios idolos encontrados con el mismo nombre",
            "searchingWiki": "La IA esta extrayendo datos de la estrella...",
            "feedbackTitle": "Chat: Reacciones y Historias del Alma",
            "feedbackDesc": "Comparta tus resultados de forma anonima! Cual es tu vibra hoy?",
            "error_msg": "Qué onda.. el motor de Saju se rompio. Intenta de nuevo.",
            "organ_map": {"Wood": "Hígado/Vesícula", "Fire": "Corazón/ID", "Earth": "Estómago/Bazo", "Metal": "Pulmón/IG", "Water": "Riñón/Vejiga"},
            "body_part_map": {"Wood": "Músculos/Ojos", "Fire": "Vasos/Lengua", "Earth": "Piel/Boca", "Metal": "Vías/Nariz", "Water": "Huesos/Oídos"},
            "exercise_map": {"Wood": "Caminar/Pilates", "Fire": "HIIT/Baile", "Earth": "Senderismo/Pesas", "Metal": "Yoga/Boxeo", "Water": "Natación/Meditación"},
            "luck_item_map": {"Wood": "Madera/Verde", "Fire": "Rojo/Sol", "Earth": "Amarillo/Tierra", "Metal": "Blanco/Metal", "Water": "Negro/Agua"},
            "star_map": {"Wood": "Árbol", "Fire": "Sol", "Earth": "Tierra", "Metal": "Diamante", "Water": "Océano"},
            "skill_map": {"Wood": "Planificación", "Fire": "Discurso", "Earth": "Coordinación", "Metal": "Análisis", "Water": "Intuición"},
            "element_labels": {"Wood": "Madera", "Fire": "Fuego", "Earth": "Tierra", "Metal": "Metal", "Water": "Agua"},
            "trait_map": {"Wood": "Vitalidad", "Fire": "Pasión", "Earth": "Tolerancia", "Metal": "Decisión", "Water": "Sabiduría"},
            "place_map": {"Wood": "Parque", "Fire": "Escenario", "Earth": "Café", "Metal": "Librería", "Water": "Ribera"},
            "season_map": {"Wood": "Primavera", "Fire": "Verano", "Earth": "Cambio de Estación", "Metal": "Otoño", "Water": "Invierno"},
            "flower_map": {"Wood": "Brote", "Fire": "Flor", "Earth": "Fruto", "Metal": "Semilla", "Water": "Raíz"},
            "industry_map": {"Wood": "Arte/Creativo", "Fire": "IT/Medios", "Earth": "Finanzas/Inmuebles", "Metal": "Tecno/Fab", "Water": "Servicio/Logística"},
            "style_map": {"Wood": "Puro", "Fire": "Llamativo", "Earth": "Estable", "Metal": "Chic", "Water": "Místico"},
            "mission_map": {"Wood": "Nuevo Desafío", "Fire": "Expresión", "Earth": "Equilibrio", "Metal": "Mejora", "Water": "Reflexión Interior"},
            "scientific_analysis": "🧬 [Análisis de Datos Científicos Next-Gen]",
            "element_weight": "Pesos de Energía de los Elementos (Proporción 100%)",
            "mbti_dynamic": "Dinámica Psicológica de Cuatro Letras MBTI",
            "rpre_hypothesis": "Hipótesis de Persona (Motor RPRE)",
            "REL_LABELS": {
                "A": "Dúo Fantástico", "B": "Pareja Estable", "C": "Compañero de Esfuerzo", "D": "Combo Único", "E": "Par de Nuevo Desafío"
            },
            "MBTI_TRAITS": {
                "E": "Extrovertido", "I": "Introvertido", "S": "Realista", "N": "Intuitivo",
                "T": "Lógico", "F": "Sensible", "J": "Planificado", "P": "Espontáneo"
            },
            "SYNERGY_LABELS": {
                "생": "Sinergia", "극": "Conflicto", "조화": "Armonía"
            },
            "MISSION_POINTS": ["encanto", "especial", "giro", "que enamora", "punto stan"]
        },
        "MBTI_FUNC_FRAGMENTS": {
            "e_i": {
                "E": "tiende a irradiar energía hacia afuera y prosperar a través de la interacción social,",
                "I": "enfoca la energía interna para crear resultados profundos y significativos,"
            },
            "n_s": {
                "N": "cree en la intuición y las posibilidades futuras para abrir caminos creativos,",
                "S": "completa escenarios perfectos basados en datos realistas y sensoriales,"
            },
            "t_f": {
                "T": "toma decisiones lógicas y objetivas para establecer estrategias óptimas,",
                "F": "conmueve corazones a través de una cálida empatía y el intercambio emocional,"
            },
            "j_p": {
                "J": "brinda confianza constante con una gestión personal sistemática y planificada,",
                "P": "disfruta de cambios flexibles y espontáneos, mostrando un encanto radiante en cualquier lugar."
            }
        },
        "RPRE_TEMPLATES": {
            "core_v1": "Sobre la poderosa esencia de {p1}, se suma el sentido sofisticado de {p2}. Si bien la estrella viste la persona de {mbti} y se muestra como tal ante el público, en momentos críticos, sale a relucir la persistencia inherente de {p1}, revelando un estilo de 'Mano de hierro en guante de seda'.",
            "hero_v2": "La base cósmica de {p1} proporciona un cimiento sólido para la chispa creativa de {p2}. Conocida públicamente como el ícono {mbti}, la verdadera fuerza de la estrella reside en una frecuencia '{element}' oculta que solo aparece bajo presión.",
            "mystic_v3": "Guiada por la intuición de {p1} y refinada por la ejecución de {p2}, la persona de {mbti} actúa como una máscara hermosa. Detrás, opera un complejo motor de equilibrio elemental, creando un campo magnético irresistible."
        },
        "MZ_ANALYSIS_FRAGMENTS": {
            "action_guides": {
                "vibe": [
                    "Crea una playlist con los temas favoritos de {idol} y compártela en SNS con tu toque MZ.",
                    "Visita un lugar que {idol} haya frecuentado y recrea su pose — misión peregrinación completada.",
                    "Encuentra el punto en común de sus gustos y mándale a {idol} esa señal de 'esto somos totalmente nosotros'.",
                    "Crea un look con los colores personales de {idol} o sus prendas favoritas. Era gemelas activada.",
                    "Escribe con caligrafía una frase de la entrevista de {idol} que te llegó al alma y publícala pa' el fandom.",
                    "Lee o mira algo que {idol} haya mencionado y comparte tu reseña MZ-style en la TL."
                ],
                "heart": [
                    "Recuerda ese habito chiquito de {idol} y tráelo en un fan meet o app de fans. Que sienta que lo ves DE VERDAD.",
                    "Escríbele una carta o mensaje de puño y letra usando palabras que eleven la fortaleza interior de {idol}. Hazlo real.",
                    "Entiende la brecha T/F de sus MBTIs y prepara las palabras exactas que {idol} necesita escuchar cuando flaquea.",
                    "Recopila las frases que le han dado fuerzas a {idol} y empaquétalas como un regalo de 'playlist de aliento'.",
                    "Planea una celebración pequeña y sincera no solo en su cumpleaños sino también en su aniversario de debut.",
                    "Edita un clip con todos los momentos en que viste crecer a {idol} — mándaselo con puro amor genuino."
                ],
                "energy": [
                    "Organiza un voluntariado con impacto o proyecto de fans en la fecha de aniversario de {idol}.",
                    "Arma una outfit o mercancía con el color personal de {idol} para sumar hype en el fandom.",
                    "Aprende el hobby que {idol} empezó últimamente, en espíritu lo hacen juntos. Nueva era, nuevo reto.",
                    "Crea tu propio video de challenge con la canción de {idol} y riega energía positiva 'pa todo el mundo.",
                    "Empieza el ejercicio que {idol} practica, registra tu progreso y comparte esa energía con el universo.",
                    "Deja un mensaje mañanero vibrante y cálido en el canal de fans de {idol} cada día. Sé su solcito diario."
                ]
            },
            "relationship_intro": [
                "Tu frecuencia sincroniza al {score}%! Un combo de {rel_label}.",
                "Señales cósmicas impactando fuerte en esta química de {rel_label}.",
                "Básicamente destino, esta vibra de {rel_label} es innegable.",
                "Los datos prueban que este match de {rel_label} es élite, puntos: {score}!",
                "La resonancia entre sus ondas crea una obra maestra de {rel_label}.",
                "Un timing de {rel_label} a través del tiempo y espacio, {score}% de probabilidad."
            ],
            "relationship_core": [
                "Una relación de libro de texto perfecta donde llenan los vacíos del otro.",
                "Una narrativa de tensión y crecimiento, como un drama juvenil de superación.",
                "Un dúo invencible que se siente como tener el mundo entero a sus pies.",
                "Las diferencias actúan como un catalizador para el crecimiento y la emoción mutua.",
                "Sincronización de almas donde una sola mirada lo dice todo.",
                "Un combo de poder positivo que puede superar cualquier obstáculo con una sonrisa."
            ],
            "bias_essence": [
                "Tiene una fuerte energía '{element}', desprendiendo un aura carismática.",
                "El rasgo dominante de '{element}' mezcla sensibilidad con dominio escénico.",
                "Como un sol cálido, es una vitamina humana que irradia energía positiva.",
                "Sólido como una roca, un ícono de 'Green Flag' que brinda confianza constante.",
                "Flexible como agua clara, posee un encanto profundo y misterioso.",
                "La fuerza del metal y el brillo de una gema, brillando con el paso del tiempo."
            ],
            "bias_point": [
                "El mayor atractivo es la brecha entre el carisma y las vibras de cachorro.",
                "Los fans aman la mezcla de 'Modo Pro' y momentos de TMI diario inesperados.",
                "Un observador silencioso cuyas raras palabras explotan con alta dopamina.",
                "El delicado amor por los fans y compartir pequeñas anécdotas roba corazones.",
                "La confianza viene de su constante automejora y crecimiento visible.",
                "Sentido visual inigualable y estética única en cada outfit."
            ],
            "bias_tmi": [
                "Siendo {mbti}, literalmente vive esa vida de dios súper organizada — este cuate planea todo mientras el resto de nosotros still vibing.",
                "Con esa energía icónica de {mbti}, recuerda la reacción más mínima del fan — ese tweet de hace 3 meses? Lo vio. Lo recuerda.",
                "Esa personalidad {mbti} significa que necesita tiempo a solas para recargarse — un gato certificado con energía de protagonista independiente.",
                "Puro caos {mbti} pero en el mejor sentido: siempre cocinando ideas creativas que dejan a los fans en shock cada vez. Total idea bank.",
                "Por fuera parece calmado, pero ese quirk inesperado de {mbti} pega diferente — VA a romper el silencio con algo descontrolado e icónico.",
                "Esa energía {mbti_trait} es tan real — sin querer se vuelve el terapeuta del grupo y todos le confían todo de forma natural."
            ],
            "recent_fortune": [
                "{idol} está en modo comeback total. Career high incoming — las estrellas literalmente se alinearon pa' este momento, sin mentiras.",
                "La suerte de interacción está SUBIENDO. Una reacción legendaria, un momento icónico con el fandom — viene y va a estar en la TL pa' siempre.",
                "Este es un arco de recarga, pero no te engañes — el aura se está poniendo PROFUNDA. Cuando vuelva, va a ser una era de brillo otoñal.",
                "Un apoyo mayor en la carrera acaba de entrar en órbita. Una collab global inesperada? El saju dice que no es SI, es CUÁNDO.",
                "La era financiera y de marca de {idol} está pegando diferente. Contratos publicitarios, proyectos solos — asegurando el bag. Stan queen/king del negocio.",
                "La pasión interna está EN SU PUNTO MÁXIMO. Lo que sea que {idol} haya estado creando por su cuenta está a punto de salir y NO pasará inadvertido."
            ],
            "synergy_why": [
                "Tu '{u_element}' y su '{i_element}' juntos son pura química — literal están saltando chispas y sirviendo fuego. 🔥",
                "Sus cartas Saju se complementan perfecto y maximizan la sinergia. Juntos son el amuleto de la suerte definitivo, no hay debate. 💅",
                "El combo de {u_mbti} y {i_mbti} cubre los puntos ciegos del otro con precisión que da escalofrío. El dúo más balanceado del chart, fr.",
                "'{u_element}' alimentando la energía '{i_element}' es básicamente una dinámica de apoyo perfecta — eres genuinamente su fuente de poder.",
                "'{u_element}' y '{i_element}' son sabores distintos que de alguna forma crean una química adictiva. El rizz es mutuo y no tiene igual.",
                "El empuje de {u_mbti} más la naturaleza detallista de {i_mbti}? Juntos son literalmente imparables. Dúo de final boss."
            ]
        },
        "PURE_LOVE_STYLES": [
            "Esta persona posee una energía inherente, profunda y misteriosa, que no puede ser capturada por tipos de personalidad estándar. Si sienten atracción hacia ti, se acercarán audazmente, priorizando el latido de su corazón y las chispas intuitivas sobre el juicio racional. Son románticos salvajes que entregan toda la pasión latente en su interior.",
            "La energía innata de su mes de nacimiento se alinea de manera única con la tuya, brindando un sentido de pertenencia profundo y estable a nivel del alma, como si estuvieran conectados desde una vida pasada. Muestran un estilo de afecto sólido y firme como una roca, brindando un apoyo interno inquebrantable.",
            "El cruce entre su Yin y Yang equilibra perfectamente el tuyo: brindando calidez cuando estás agotado y un balance fresco e instintivo cuando estás abrumado. Sin necesidad de técnicas llamativas, actúan como una llave maestra para tu alma, llenando tus vacíos emocionales a través de su frecuencia natural."
        ],
        "PURE_SYNERGY": {
            "생": "[Crecimiento Armonioso] Su energía inherente actúa como una línea de suministro impecable que nutre tu alma. El simple hecho de coexistir amplifica las vibraciones positivas, desbloqueando un potencial sin precedentes y una enorme fortuna: una sinergia cósmica milagrosa.",
            "극": "[Choque Intenso] A veces sus energías chocan fuertemente, pero esta misma fricción genera una inmensa fuerza creativa que impulsa poderosamente el crecimiento de ambos. Es un destino fascinante en el que se complementan en medio de una atracción visceral e innegable.",
            "비화": "[Almas Gemelas Espejo] Un vínculo sólido formado por la unión de elementos idénticos. Son socios que crean su propio y vasto universo a través de una resonancia profunda que no necesita explicación. Como gemelos de una vida pasada, sus almas comparten el mismo matiz, convirtiéndose en un refugio para toda la vida."
        },
        "PURE_TIPS": [
            "Al acercarte a ellos, deja de lado los coqueteos calculados o las estrategias manuales. Simplemente irradia el encanto puro de tu elemento base natural (Madera/Fuego/Tierra/Metal/Agua). Ahí es cuando sentirán la atracción más poderosa hacia ti.",
            "En lugar de eventos muy preparados o habilidades de conversación elocuentes, las frecuencias cósmicas de ambos se sincronizan perfectamente en momentos físicos compartidos, como mirar en silencio el cielo nocturno o caminar por la naturaleza.",
            "En lugar de dejarte llevar por su exterior o factores situacionales, muéstrales una confianza constante, como si vieras directamente la esencia de su alma. Enviarles un apoyo interno incondicional y silencioso es la llave maestra absoluta para abrir las puertas más profundas de su corazón."
        ],
        "MONTH_KEYWORDS": [
            "Vitalidad de Madera", "Pico de Fuego", "Cosecha de Metal", "Sabiduría de Agua", "Modo Dios",
            "Vitalidad de Madera", "Pico de Fuego", "Cosecha de Metal", "Sabiduría de Agua", "Modo Dios",
            "Vitalidad de Madera", "Pico de Fuego"
        ],
        "MONTH_DESCS": [
            "[Vitalidad Madera] Nuevas Semillas: La energía del renacer da vida a tu trabajo. Mes perfecto para iniciar proyectos.",
            "[Pico de Fuego] Explosión de Pasión: La energía alcanza su cenit. Resuelve tareas pendientes con un impulso poderoso.",
            "[Cosecha Metal] Decisión Fría: Se vuelve claro qué descartar y qué mantener. La eficiencia es tu arma.",
            "[Sabiduría Agua] Acumulación de Sabiduría: Tiempo de almacenar energía interna y conocimiento profundo.",
            "[Modo Dios] Tu era ha llegado: looks, skills y suerte están en su ápice. Arrasa!",
            "[Crecimiento Madera] Potencial en Flor: Tus ideas creativas comienzan a ganar tracción. Comparte tu visión.",
            "[Brillo de Fuego] Foco Radiante: Eres el centro de atención. Excelente para eventos sociales y networking.",
            "[Precisión Metal] Enfoque Agudo: Gran momento para planeación financiera o upgrades técnicos.",
            "[Flujo de Agua] Ritmo Natural: Suelta el concepto de control y fluye con la marea. Suerte inesperada te espera.",
            "[Equilibrio Tierra] Suelo Firme: Mes para estabilizar cimientos y nutrir relaciones importantes.",
            "[Espíritu Madera] Chispa Interior: Revitaliza tus hobbies. Una nueva perspectiva trae un gran avance.",
            "[Núcleo de Fuego] Calor Interior: Enfócate en tu bienestar personal. La energía radiante comienza en tu centro."
        ],
        "LIFETIME_STAGES": {
            "Wood": {
                "youth": "[Inicial: Brote de Primavera] Periodo de gran curiosidad y deseo de aprender. En tus 10s y 20s, florecerás con ayuda de otros.",
                "young_adult": "[Juventud: Árbol Exuberante] Estableciendo tu propio dominio en la sociedad. En tus 30s y 40s, alcanzarás tu pico con gran impulso.",
                "middle_age": "[Madurez: Raíces Fuertes] La experiencia acumulada da frutos, brindando estabilidad. En tus 50s y 60s, brillarás como líder o mentor.",
                "senior": "[Vejez: Bosque Rico] Respetado por los demás, viviendo en paz. Después de los 70s, vendrán el ocio mental y el honor."
            },
            "Fire": {
                "youth": "[Inicial: Llama Ardiente] Un periodo apasionado y creativo. En tus 10s y 20s, te harás notar a través de actividades destacadas.",
                "young_adult": "[Juventud: Sol del Mediodía] Tu periodo más activo con resultados explosivos. En tus 30s y 40s, liderarás el cambio y crearás tendencias.",
                "middle_age": "[Madurez: Lámpara Suave] Controlando la pasión interna para iluminar sabiamente tu entorno. En tus 50s y 60s, liderarás organizaciones.",
                "senior": "[Vejez: Atardecer Hermoso] Viviendo como un sabio asesor. Después de los 70s, hallarás felicidad en la cultura, el arte o el descanso espiritual."
            },
            "Earth": {
                "youth": "[Inicial: Nutriente de la Tierra] Construyendo bases y ganando confianza. En tus 10s y 20s, tus esfuerzos silenciosos darán logros.",
                "young_adult": "[Juventud: Tierra Fértil] Cooperando con many y creando riqueza. En tus 30s y 40s, te enfocarás en activos estables y familia.",
                "middle_age": "[Madurez: Gran Montaña] Liderando grandes organizaciones con convicción inquebrantable. En tus 50s y 60s, ganarás fama como mediador.",
                "senior": "[Vejez: Vasta Tierra] Sintiéndote recompensado al compartir. Después de los 70s, disfrutarás de una vejez pacífica y descendencia próspera."
            },
            "Metal": {
                "youth": "[Inicial: Hoja Afilada] Desarrollando metas claras y decisión. En tus 10s y 20s, destacarás ganando ventaja en la competencia.",
                "young_adult": "[Juventud: Brillo de Gema] Probando tu valor con sentido sofisticado. En tus 30s y 40s, reunirás gran riqueza basada en estándares claros.",
                "middle_age": "[Madurez: Acero Fuerte] Teniendo la autoridad para lograr cualquier cosa. En tus 50s y 60s, ejercerás poder en la cima de la estrategia.",
                "senior": "[Vejez: Oro Noble] Manteniendo una vida digna y enfoque en la completitud interna. Después de los 70s, vivirás cómodo resumiendo tu vida."
            },
            "Water": {
                "youth": "[Inicial: Manantial Claro] Sabio e inteligente, superando expectativas. En tus 10s y 20s, dominarás campos con pensamiento flexible.",
                "young_adult": "[Juventud: Río Sinuoso] Ganando experiencia en el mundo ancho. En tus 30s y 40s, atraparás oportunidades inesperadas mediante el cambio.",
                "middle_age": "[Madurez: Lago Profundo] Convirtiéndote en guía espiritual con vasto conocimiento. En tus 50s y 60s, expandirás tu influencia silenciosamente.",
                "senior": "[Vejez: Mar Infinito] Hallando paz con un corazón amplio como el mar. Después de los 70s, hallarás alegría en viajes o estudios."
            }
        },
                "TIP_COMPONENTS": {
            "actions": [
                "Con la honestidad característica de {mbti}, sin juegos de manipulación",
                "Canalizando la energía positiva de {u_el} para impulsarse mutuamente",
                "Planeando un evento sorpresa en {place} que nadie espera",
                "Respetando cada pequeño rasgo {mbti_trait} — ahí está la magia real",
                "Disfrutando sesiones de {exercise} en privado, solo ustedes dos",
                "Sincronizando la vibra cuando la energía de {star} está en su punto máximo",
                "Soltando un humor {mbti}-coded totalmente inesperado de vez en cuando",
                "Manteniendo ese aura clásica y estable de {mbti_trait} que te define",
                "Llegando con el {luck_item} favorito del star — eso es cumplir el nivel",
                "Mostrando tu {skill} de nivel pro para que lo note",
                "Siendo el rey/reina de las reacciones genuinas — esa es tu vibra",
                "Priorizando el cuidado de {organ} primero — el bienestar es el glow-up real",
                "Haciendo una peregrinación juntos a los lugares sagrados de {place}",
                "Escribiendo una carta sincera que celebre el {trait} del star",
                "Manteniendo esa vibe cool y única de {mbti} que te hace iconique"
            ],
            "topics": [
                "elogiar la energía magnética de {trait} del star",
                "aprovechar la sinergia elemental {u_el}/{i_el} que los une",
                "preocuparte primero por el bienestar de {organ} del star",
                "activar el poder del {luck_item} que el star más atesora",
                "compartir consejos genuinos y reflexivos sobre {skill}",
                "proponer un tour juntos por {place}",
                "intercambiando las lecturas de fortuna de {star} entre ustedes",
                "hypeando el lado {mbti_trait} del star — necesita escucharlo",
                "mencionando esa palabra clave de {trait} de una entrevista antigua",
                "spileando todo sobre la obsesión #1 del star con {luck_item}",
                "proponiendo un challenge de {exercise} en dúo",
                "regalando un ítem de color de suerte que conecte con la energía {u_el} del star"
            ],
            "results": [
                "el cheat code definitivo para inundar la relación de dopamina.",
                "el secreto para sincronizar sus almas en la misma frecuencia.",
                "el camino para plantar una green flag inquebrantable de certeza.",
                "el movimiento que fortalece el hilo del destino que existe desde vidas pasadas.",
                "el atajo más rápido para convertirte en su persona #1.",
                "la pieza final que completa la química exclusiva entre ustedes.",
                "la forma de crear una sinergia de nivel god que acelera el corazón.",
                "el método para convertirse en personajes principales del destino del otro.",
                "la señal definitiva que responde al opening line no dicho del star.",
                "la estrategia para amplificar la sinergia de {rel_type} al 200%."
            ]
        },
        "GEN_MISSION_COMPONENTS": {
            "actions": {
                "E": [
                    "Compartiendo una foto de {target} en la comunidad", "Promocionando a full el encanto {trait} del star", 
                    "Sumándote a un reto viral en redes", "Transmitiendo en vivo desde un {place} icónico",
                    "Creando y difundiendo memes {mbti} del star", "Haciendo el reto de {exercise} con el fandom",
                    "Yendo a ver el anuncio de cumple del star y subiendo foto", "Dando ideas para hacer merch grupal",
                    "Grabándote gritando el fanchant del nuevo comeback", "Llorando brillitos imaginando un momento {point} con el star"
                ],
                "I": [
                    "Haciendo journaling de {target} a solas", "Haciendo maratón de fancams de su era {trait}",
                    "Pasando tiempo a solas en el {place} que mencionó el star", "Meditando con la playlist del star",
                    "Escribiendo una carta súper sincera para el star", "Coleccionando en secreto el {luck_item} del star",
                    "Guardando un registro privado de sus vibes {mbti}", "Bingeando fancams en casa sin parar",
                    "Analizando su fortuna {star} para usarlo de amuleto", "Escribiendo las palabras tan lindas que dijo el star"
                ]
            },
            "targets": {
                "Wood": ["merch temática de plantitas verdes", "lugar de peregrinación con olor a bosque", "video de su era de crecimiento", "lucky item color verde"],
                "Fire": ["ítem rojo súper llamativo", "fancam de un stage que arde", "lugar con una vista nocturna deslumbrante", "escena de pura pasión"],
                "Earth": ["merch beige súper aesthetic", "lugar tranqui con vibra earthy", "foto de su vida diaria", "registro de su esfuerzo constante"],
                "Metal": ["accesorio plateado chic", "sesión de fotos con carisma afilado", "lugar de diseño minimalista", "entrevista que muestra su voluntad de hierro"],
                "Water": ["photocard con vibra de océano azul", "sesión de radio relajante con lluvia", "canción lenta que te deja pensando", "ítem con vibra transparente y clara"]
            },
            "contexts": [
                "¡Amplifica su sinergia de {rel_type} al 200%!", "Disfruta el momento en que sus frecuencias del destino se sincronizan.",
                "Haz aún más fuerte el hilo rojo de su vida pasada.", "El atajo más rápido para ser su #1.",
                "Completa la green flag definitiva.", "Sincroniza tu energía con la vibra {u_el} del star.",
                "La pieza final para su química secreta.", "Experimenta la sinergia god-tier que hace latir tu corazón.",
                "Conviértete en su bestie definitivo.", "La magia para convertir sus diferencias en un encanto {point}."
            ]
        },
        "MISSION_COMPONENTS": {
            "labels": [
                "Misión Etapa {n}: {u_mbti} x {i_mbti}",
                "Fusión de Energía {u_el} & {i_el}",
                "Escapar del Período de Negación Stan: {point}",
                "Activar el Buff de Protagonista: {point}",
                "Sincronización de Frecuencia del Destino",
                "Guía de Estrategia {i_mbti} Personalizada",
                "Romper el Techo de Química: {point}",
                "Foto Prueba del Alma Gemela",
                "Misión Carga Total de Dopamina",
                "Rutina de Sinergia God-Tier",
                "Escapar del Estacionamiento de Vidas Pasadas: {point}",
                "Desbloquear el Campo de Fuerza de {trait} del Star",
                "Caminar Juntos por el Sendero de {rel_type}"
            ],
            "reasons": [
                "En K-saju, {u_el} crea y soporta a {i_el} — ese es su blueprint del destino.",
                "La energía {mbti_trait} de {u_mbti} es un estímulo fresco que el star necesita.",
                "Esto repara el punto de tensión donde las energías de {organ} chocan.",
                "Es la solución para arreglar el pequeño desajuste del mapa de vidas pasadas.",
                "La energía {star} del star está resonando con tu frecuencia {u_el} ahora mismo.",
                "Esto lleva la sinergia de {rel_type} entre ustedes a su nivel absoluto máximo.",
                "La vibra {mbti} del star está lowkey obsesionada con tu energía {mbti_trait}."
            ],
            "tasks": {
                "vibe": [
                    "Crear merch personalizado centrado en el {trait} icónico del star",
                    "Decorar tu diario con fotocards que muestren tu compatibilidad {mbti}",
                    "Recrear una foto en {place} que el star mencionó, en la misma pose exacta",
                    "Aprender realmente el {skill} con el que el star actualmente está obsesionado",
                    "Presumir un {luck_item} que haga match con la paleta de color personal del star",
                    "Escribir la frase más icónica del star en caligrafía y compartirla",
                    "Streamear {n} veces el nuevo escenario del star y publicar prueba",
                    "Crear un meme viral sobre los momentos cotidianos {mbti}-coded del star"
                ],
                "heart": [
                    "Hacer tag masivo en el hashtag de SNS para apoyar la salud de {organ} del star",
                    "Enviar un mensaje de apoyo genuinamente {mbti_trait} y desde el corazón",
                    "Regalar un ítem similar al {luck_item} que el star más atesora",
                    "Escribir caligrafía alabando el aura de {star} del star",
                    "Ver en maratón los videos de la era debut del star sobre {trait}",
                    "Enviar exactamente las palabras cálidas de consuelo que el star merece oír",
                    "Escribir una carta a mano analizando la personalidad {mbti} del star y postearla",
                    "Darse un momento de autoapreciación por apoyar pacientemente el crecimiento del star"
                ],
                "energy": [
                    "Postear prueba del workout con la mentalidad de hacer {exercise} junto al star",
                    "Vestirse de un color de suerte alineado con la energía {i_el} del star",
                    "Editar un video de {n} minutos que capture la narrativa épica del star",
                    "Confiar en la sinergia {u_el}/{i_el} y aceptar un nuevo desafío personal",
                    "Meditar con la playlist del star y limpiar tu campo de energía",
                    "Vivir tu mejor vida como el star lo haría — anotarlo y compartir prueba",
                    "Lucir tu outfit diario con el ítem de suerte de {star} del star",
                    "Hablarle a al menos una persona hoy sobre la magia de {trait} del star"
                ]
            }
        },
        "SYNERGY_MISSIONS": {
            "analysis_1": {
                "label": "Deep Analysis: {point_1} 📸",
                "boost": 15,
                "reason": "Comprensión profunda basada en {reason_1}.",
                "tasks": ["{task_1_1}", "{task_1_2}", "{task_1_3}"]
            },
            "analysis_2": {
                "label": "Soul Sync: {point_2} 💬",
                "boost": 15,
                "reason": "Resonancia espiritual a través de {reason_2}.",
                "tasks": ["{task_2_1}", "{task_2_2}", "{task_2_3}"]
            },
            "analysis_3": {
                "label": "Cosmic Action: {point_3} 🎡",
                "boost": 20,
                "reason": "Actividades de sanación para {reason_3}.",
                "tasks": ["{task_3_1}", "{task_3_2}", "{task_3_3}"]
            }
        },
        "EXPERT_ADVICE": {
            "Health": [
                "Agente A (Tradicional): Tu elemento sugiere una debilidad en el área de {organ}. El Saju tradicional recomienda tés de hierbas para equilibrar tu energía interna.",
                "Agente B (Psicológico): El estrés tiende a manifestarse en tu {body_part}. Prioriza momentos de calma y meditación profunda para evitar el agotamiento.",
                "Agente C (Tendencia): Prueba {exercise}, tendencia en Seúl. Es el flujo perfecto para circular tu tipo de energía específica."
            ],
            "Wealth": [
                "Agente A (Legado): Una fuerte alineación financiera ocurre en el mes {month}. Esta es tu oportunidad para inversiones a largo plazo.",
                "Agente B (Conductual): Tiendes a gastar impulsivamente cuando tu energía es alta. Establece una 'Regla de Espera' para compras grandes.",
                "Agente C (Tech): Usar un accesorio con temática de {luck_item} actuará como un imán de suerte para tus ingresos secundarios."
            ],
            "Career": [
                "Agente A (Autoridad): Tu carta muestra la energía de 'La {star}'. Eres un líder nato destinado a la alta dirección.",
                "Agente B (Social): Tu estilo de networking es tu arma más afilada. Enfoquémonos en el 'Poder Blando' para ganarte a colegas difíciles.",
                "Agente C (Skill): Mejorar en {skill} es tu código secreto para 2026. Esta sinergia activará un cambio masivo en tu carrera."
            ],
            "Love": [
                "Agente A (Destino): Tienes una conexión predestinada con alguien con energía de '{element}'. Son la pieza que te falta.",
                "Agente B (Aura): Tu mayor encanto es tu '{trait}'. Úsalo en tus citas; es lo que te hace inolvidable.",
                "Agente C (Vibe): Se predice un encuentro de alta probabilidad en un {place}. Mantén tu energía de protagonista cuando lo visites."
            ]
        },
        "LIFETIME_EXPERTS": [
            {
                "name": "Maestro Cheong",
                "focus": "Ciclo Mayor y Equilibrio Elemental",
                "comment": "Tu destino fluye con la energía de {season}. Como un gran río, superarás los obstáculos y alcanzarás tu éxito en la segunda mitad de la vida."
            },
            {
                "name": "Dra. Jung",
                "focus": "Temperamento Interno y Flujo Emocional",
                "comment": "Tienes el alma delicada de una {flower}. Nunca dudes de tu frecuencia única; tu sensibilidad es en realidad tu mayor poder."
            },
            {
                "name": "Neo",
                "focus": "Aptitud Tecnológica y Lógica de Riqueza",
                "comment": "Tu algoritmo de energía está optimizado para el sector de {industry}. Posees el ojo analítico para identificar riqueza oculta."
            },
            {
                "name": "Sophie",
                "focus": "Profundidad de Relación y Resonancia",
                "comment": "En el amor, transmites vibras de '{style}'. Puede que te cueste expresar sentimientos, mas una vez comprometido, eres un compañero legendario."
            },
            {
                "name": "Maestro Zen",
                "focus": "Misión de Vida y Alineación Holística",
                "comment": "Tu misión final no es solo el éxito, sino '{mission}'. Tu aura clara guiará naturalmente a otros y creará un efecto positivo."
            }
        ],
        "MONTH_FORTUNES": {
            "1": {
                "theme": "Vibra de Nuevos Comienzos, Energía de '{dominant}' 🌱",
                "signal": "El mejor mes para poner metas con {idol}. La sinergia va a explotar!",
                "guide": "Modo Dios activado! Empieza con 10min de lectura o ejercicio. 💰 La riqueza sube!"
            },
            "2": {
                "theme": "Logro Intelectual y Reflexión 📚",
                "signal": "Te inspirarás por el lado inteligente de {idol}. Charlas profundas aseguradas.",
                "guide": "Invierte en aprender. Nuevas certs o estudio serán un activo gigante."
            },
            "3": {
                "theme": "Vitalidad de Primavera y Expansión Social 🌸",
                "signal": "Momento perfecto para eventos al aire libre con {idol}.",
                "guide": "Nuevas conexiones vienen en camino. Sé sociable. 💓 Vibras de amor UP!"
            },
            "4": {
                "theme": "Energía Apasionada y Crecimiento ⚡",
                "signal": "La pasión de {idol} te va a motivar. Tomen el reto juntos!",
                "guide": "Empieza lo que postergaste. La ejecución ahora decide tus resultados finales."
            },
            "5": {
                "theme": "Estabilidad y Paz Interior ⛰️",
                "signal": "Gran mes para relajarse y construir un vínculo profundo con {idol}.",
                "guide": "Limpia tu espacio. Un entorno claro significa un flujo claro de suerte."
            },
            "6": {
                "theme": "Explosión de Comunicación e Ideas 💡",
                "signal": "Espera noticias divertidas o una interacción sorpresa con {idol}.",
                "guide": "Anota tus ideas. Un pensamiento pequeño puede ser un proyecto masivo."
            },
            "7": {
                "theme": "Emociones Intensas e Intuición al Pico 🌊",
                "signal": "Tu frecuencia de destino con {idol} se vuelve más fuerte. Modo stan puro.",
                "guide": "Confía en tu instinto. La respuesta ya está dentro de tu brújula espiritual."
            },
            "8": {
                "theme": "Preludio de Cosecha y Abundancia ⚔️",
                "signal": "Celebra los logros de {idol} y comparte energía positiva.",
                "guide": "Enfócate en tu salud. Los hábitos regulares cargarán tu espíritu base."
            },
            "9": {
                "theme": "Juicio Cuidadoso y Metas 🎯",
                "signal": "Revisa tus planes de fin de año con {idol} y sincroniza tus vibras.",
                "guide": "Cuida tu bolsillo. Corta gastos inútiles para hallar mejores oportunidades."
            },
            "10": {
                "theme": "Entendimiento Profundo y Crecimiento 🔮",
                "signal": "Entenderás el mensaje oculto o el corazón de {idol} hoy.",
                "guide": "Escribe un diario o medita. La suerte se abre cuando escuchas tu interior."
            },
            "11": {
                "theme": "Ola de Cambio y Tácticas Flexibles 🌊",
                "signal": "Apoya las nuevas actividades de {idol} e intercambia energía cósmica.",
                "guide": "Sigue el flujo. El crecimiento viene cuando no temes al cambio."
            },
            "12": {
                "theme": "Terminar y Descansar para Nuevos Sueños ❄️",
                "signal": "Un mes cálido para cerrar el año con el corazón lleno por {idol}.",
                "guide": "Tiempo de treat! Premiarte mantiene tu energía al máximo."
            }
        },
        "MZ_SAJU_DICTIONARY": {
            "일주": "¡La energía del día en que naciste! El 'vibe' central de tu Saju, tu verdadero yo.",
            "용신": "Tu suprema energía 'amuleto de la suerte'. ¡Potenciarla baja la dificultad de la vida al instante!",
            "기구신": "La sutil energía 'villana'. Manéjala bien para proteger tu paz mental.",
            "상생": "Una dinámica de mejores amigos con apoyo mutuo. La definición de 'hacemos clic'.",
            "상극": "Química picante donde la fricción crea pura energía imparable.",
            "도화살": "Energía de protagonista. Un aura natural que atrae todas las miradas.",
            "역마살": "Vibra de trotamundos global. ¡No te quedas quieto y el movimiento te trae éxito masivo!",
            "현침살": "El supremo 'verificador de datos'. Perspicacia aguda y atención al detalle inigualable.",
            "비견": "Energía de colega alma gemela. Aumenta tu equipo y amigos confiables.",
            "겁재": "Impulso competitivo. ¡Tener un poco de rivalidad te hace crecer rapidísimo!",
            "편인": "El peculiar 'banco de ideas'. Pensamiento fuera de la caja que es tu encanto único.",
            "정인": "Nacido para ser amado. La vibra del consentido que recibe cariño donde sea.",
            "식신": "Talento desbordante y buena suerte para la comida. El máximo disfrutador de la vida productiva.",
            "상관": "Innovador rebelde. ¡Rompe las reglas y odia ser encasillado—puro caos creativo!",
            "편재": "Energía de premio gordo inesperado. Flex a gran escala en busca de resultados enormes.",
            "정재": "El constante y confiable 'libro contable humano'. Construye su imperio paso a paso.",
            "편관": "Líder carismático nacido tras superar pruebas extremas. Alto riesgo, recompensa legendaria.",
            "정관": "El seguidor de reglas de manual. Vibra de estudiante perfecto con principios inquebrantables."
        }
    },
    "pt": {
        "ENERGY_TRAITS": {
            "Wood": {
                "name": "Crescimento Imbatível (Wood) 🌲",
                "desc_intro": [
                    "Você literalmente emana aquela 'Energia de Protagonista' de uma árvore gigante."
                ],
                "desc_core": {
                    "default": [
                        "Totalmente focado em crescer. Vibes de produtividade 100%."
                    ]
                },
                "desc_career": [
                    "[Mente de CEO]\nSeu lugar é onde você pode criar e liderar."
                ],
                "desc_advice": [
                    "[Guia Glow-up]\nFoque em um objetivo por vez para dominar o jogo."
                ]
            },
            "Fire": {
                "name": "Chama Ardente (Fire) 🔥",
                "desc_intro": [
                    "Sua alma tem vibes super fortes de 'Sol'."
                ],
                "desc_core": {
                    "default": [
                        "A alma da festa, energia vibrante e zero filtro."
                    ]
                },
                "desc_career": [
                    "Nascido para o palco e para brilhar."
                ],
                "desc_advice": [
                    "Pense 3 segundos antes de agir no calor do momento."
                ]
            },
            "Earth": {
                "name": "Terra Sólida (Earth) ⛰️",
                "desc_intro": [
                    "Sua alma é como a vasta terra que acolhe tudo."
                ],
                "desc_core": {
                    "default": [
                        "A bateria externa dos seus amigos, equilíbrio total."
                    ]
                },
                "desc_career": [
                    "Mestre em organizar e estabilizar sistemas."
                ],
                "desc_advice": [
                    "Não se esqueça de cuidar de si mesmo também."
                ]
            },
            "Metal": {
                "name": "Espada Afiada (Metal) ⚔️",
                "desc_intro": [
                    "Sua alma grita 'Joia Pura' e 'Lâmina Afiada'."
                ],
                "desc_core": {
                    "default": [
                        "Racional e focado, lealdade absurda ao seu círculo."
                    ]
                },
                "desc_career": [
                    "Brilha com números e lógica pesada."
                ],
                "desc_advice": [
                    "Seja mais flexível consigo mesmo, perfeccionismo cansa."
                ]
            },
            "Water": {
                "name": "Fluxo Livre (Water) 🌊",
                "desc_intro": [
                    "Sua alma flui com a profundidade do oceano."
                ],
                "desc_core": {
                    "default": [
                        "Adaptabilidade total, mestre em ler as pessoas."
                    ]
                },
                "desc_career": [
                    "Nômade digital, pesquisador, criativo nato."
                ],
                "desc_advice": [
                    "Pare de pensar demais e 'toque na grama' (aja)."
                ]
            }
        },
        "MONTH_FORTUNES": {
            "1": {
                "theme": "Vibe de Novos Começos, Energia de '{dominant}' 🌱",
                "signal": "Melhor mês para definir metas com {idol}. A sinergia vai explodir!",
                "guide": "Modo Deus ativado! Comece com 10min de leitura ou exercício. 💰 Riqueza em alta!"
            },
            "2": {
                "theme": "Conquista Intelectual e Reflexão 📚",
                "signal": "Você se inspirará pelo lado inteligente de {idol}. Papos profundos garantidos.",
                "guide": "Invista em aprender. Novos certificados ou estudo serão um ativo gigante."
            },
            "3": {
                "theme": "Vitalidade da Primavera e Expansão Social 🌸",
                "signal": "Momento perfeito para eventos ao ar livre com {idol}.",
                "guide": "Novas conexões vêm por aí. Seja sociável. 💓 Vibes de amor UP!"
            },
            "4": {
                "theme": "Energia Apaixonada e Crescimento ⚡",
                "signal": "A paixão de {idol} vai te motivar. Aceitem o desafio juntos!",
                "guide": "Comece o que você adiou. A execução agora decide seus resultados finais."
            },
            "5": {
                "theme": "Estabilidade e Paz Interior ⛰️",
                "signal": "Ótimo mês para relaxar e construir um vínculo profundo com {idol}.",
                "guide": "Limpe seu espaço. Um ambiente claro significa um fluxo claro de sorte."
            },
            "6": {
                "theme": "Explosão de Comunicação e Ideias 💡",
                "signal": "Espere notícias divertidas ou uma interação surpresa com {idol}.",
                "guide": "Anote suas ideias. Um pensamento pequeno pode ser um projeto massivo."
            },
            "7": {
                "theme": "Emoções Intensas e Intuição no Pico 🌊",
                "signal": "Sua frequência de destino com {idol} fica mais forte. Modo stan puro.",
                "guide": "Confie no seu instinto. A resposta já está dentro da sua bússola espiritual."
            },
            "8": {
                "theme": "Prelúdio de Colheita e Abundância ⚔️",
                "signal": "Celebre as conquistas de {idol} e compartilhe energia positiva.",
                "guide": "Foque na sua saúde. Hábitos regulares carregarão seu espírito base."
            },
            "9": {
                "theme": "Julgamento Cuidadoso e Metas 🎯",
                "signal": "Revise seus planos de fim de ano com {idol} e sincronize suas vibes.",
                "guide": "Cuide do seu bolso. Corte gastos inúteis para achar melhores chances."
            },
            "10": {
                "theme": "Entendimento Profundo e Crescimento 🔮",
                "signal": "Você entenderá a mensagem oculta ou o coração de {idol} hoje.",
                "guide": "Escreva um diário ou medite. A sorte se abre quando você ouve seu interior."
            },
            "11": {
                "theme": "Onda de Mudança e Táticas Flexíveis 🌊",
                "signal": "Apoie as novas atividades de {idol} e troque energia cósmica.",
                "guide": "Siga o fluxo. O crescimento vem quando você não teme a mudança."
            },
            "12": {
                "theme": "Terminar e Descansar para Novos Sonhos ❄️",
                "signal": "Um mês caloroso para fechar o ano com o coração cheio por {idol}.",
                "guide": "Tempo de treat! Premiar-se mantém sua energia no máximo."
            }
        },
        "LIFETIME_STAGES": {
            "Wood": {
                "youth": "[Início: Broto de Primavera] Um período de alta curiosidade e desejo de aprender. Aos 10 e 20 anos, você florescerá com ajuda de outros.",
                "young_adult": "[Juventude: Árvore Viçosa] Estabelecendo seu próprio domínio na sociedade. Aos 30 e 40 anos, atingirá seu auge com forte impulso.",
                "middle_age": "[Maturidade: Raízes Fortes] A experiência acumulada dá frutos, gerando estabilidade. Aos 50 e 60 anos, brilhará como líder ou mentor.",
                "senior": "[Velhice: Floresta Rica] Respeitado pelos outros, vivendo em paz. Após os 70 anos, lazer mental e honra seguirão."
            },
            "Fire": {
                "youth": "[Início: Chama Ardente] Um período apaixonado e criativo. Aos 10 e 20 anos, marcará sua presença com atividades envolventes.",
                "young_adult": "[Juventude: Sol do Meio-dia] Seu período mais ativo com resultados explosivos. Aos 30 e 40 anos, liderará mudanças e criará tendências.",
                "middle_age": "[Maturidade: Lâmpada Suave] Controlando a paixão interna para iluminar o ambiente. Aos 50 e 60 anos, liderará como centro da organização.",
                "senior": "[Velhice: Pôr do Sol Lindo] Vivendo como consultor sábio. Após os 70 anos, encontrará felicidade na cultura, arte ou descanso espiritual."
            },
            "Earth": {
                "youth": "[Início: Nutriente da Terra] Construindo bases e ganhando confiança. Aos 10 e 20 anos, esforços silenciosos trarão conquistas.",
                "young_adult": "[Juventude: Terra Fértil] Cooperando com muitos e gerando riqueza. Aos 30 e 40 anos, focará em ativos estáveis e família.",
                "middle_age": "[Maturidade: Montanha Grande] Liderando grandes organizações com convicção inabalável. Aos 50 e 60 anos, ganhará fama como mediador.",
                "senior": "[Velhice: Vasta Terra] Sentindo recompensa ao compartilhar. Após os 70 anos, desfrutará de uma velhice pacífica e descendência próspera."
            },
            "Metal": {
                "youth": "[Início: Lâmina Afiada] Desenvolvendo metas claras e decisão. Aos 10 e 20 anos, se destacará ganhando vantagem na competição.",
                "young_adult": "[Juventude: Brilho de Gema] Provando seu valor com senso sofisticado. Aos 30 e 40 anos, reunirá riqueza baseada em padrões claros.",
                "middle_age": "[Maturidade: Aço Forte] Tendo a autoridade para realizar qualquer coisa. Aos 50 e 60 anos, exercerá poder no auge da estratégia.",
                "senior": "[Velhice: Ouro Nobre] Mantendo uma vida digna e foco na completude interna. Após os 70 anos, viverá confortável resumindo sua vida."
            },
            "Water": {
                "youth": "[Início: Nascente Clara] Sábio e inteligente, superando expectativas. Aos 10 e 20 anos, dominará campos com pensamento flexível.",
                "young_adult": "[Juventude: Rio Sinuoso] Ganhando experiência no mundo amplo. Aos 30 e 40 anos, pegará chances inesperadas através de mudanças.",
                "middle_age": "[Maturidade: Lago Profundo] Tornando-se guia espiritual com vasto conhecimento. Aos 50 e 60 anos, expandirá sua influência silenciosamente.",
                "senior": "[Velhice: Mar Infinito] Achando paz com um coração generoso como o mar. Após os 70 anos, achará alegria em viagens ou estudos."
            }
        },
        "MONTH_DESCS": [
            "[Vitalidade Madeira] Novas Sementes: A energia do renascer dá vida ao seu trabalho. Mês perfeito para iniciar projetos.",
            "[Pico de Fogo] Explosão de Paixão: A energia atinge o seu auge. Resolva tarefas com um impulso poderoso.",
            "[Colheita Metal] Decisão Fria: Torna-se claro o que descartar e o que manter. Eficiência é sua arma.",
            "[Sabedoria Água] Acúmulo de Sabedoria: Tempo de armazenar energia interna e conhecimento profundo.",
            "[Modo Deus] Sua era chegou: looks, skills e sorte estão no seu ápice. Arrase!",
            "[Crescimento Madeira] Potencial em Flor: Suas ideias criativas começam a ganhar tração. Compartilhe sua visão.",
            "[Brilho de Fogo] Holofote Radiante: Você é o centro das atenções. Excelente para eventos sociais e networking.",
            "[Precisão Metal] Foco Aguçado: Ótimo momento para planejamentos financeiros ou upgrades técnicos.",
            "[Fluxo de Água] Ritmo Natural: Solte o controle e flua com a maré. Sorte inesperada te espera.",
            "[Equilíbrio Terra] Solo Firme: Mês para estabilizar alicerces e nutrir relacionamentos importantes.",
            "[Espírito Madeira] Faísca Interior: Revitalize seus hobbies. Uma nova perspectiva traz um grande avanço.",
            "[Núcleo de Fogo] Calor Interior: Foque no seu bem-estar pessoal. A energia radiante começa no seu centro.",
            "[Ambição Madeira] Árvores Altas: Mire alto. Seu status sobe enquanto você assume mais responsabilidade.",
            "[Festa de Fogo] Calor Social: Tempo de celebração. Conexões feitas agora serão valiosas depois.",
            "[Fio de Metal] Resultado Polido: Seu trabalho duro rende frutos visíveis. O perfeccionismo é premiado.",
            "[Profundidade Água] Tesouro Oculto: Descoberta de novo talento ou paixão. Olhe sob a superfície.",
            "[Raiz de Terra] Crescimento Estável: Progresso lento mas seguro. Não apresse o tempo da natureza.",
            "[Fluxo Natural] Mudança Sazonal: Adaptabilidade é a chave. Mude sua estratégia para o novo mood.",
            "[Artesanato Madeira] Esculpindo Sucesso: Trabalho meticuloso leva a uma vitória artística ou técnica.",
            "[Pulso de Fogo] Ação Rítmica: Mantenha o impulso. Consistência torna pequenas vitórias lendas.",
            "[Lógica Metal] Pivô Estrutural: Reorganize sua vida para o máximo rendimento. A lógica vence.",
            "[Sonho de Água] Chamado Intuitivo: Confie no seu instinto. Um encontro misterioso pode mudar tudo.",
            "[Escudo Terra] Era de Proteção: Defenda sua paz. Bom para impor limites e autocuidado.",
            "[Era Dourada] Brilho Desbloqueado: Tudo o que você toca vira ouro. Seja ousado e tome as rédeas.",
            "[Primavera Madeira] Novo Começo: Limpe o velho para o novo. Alta clareza mental.",
            "[Chama de Fogo] Brilho Breve: Um projeto curto traz reconhecimento masivo. Mova-se rápido.",
            "[Frio Metal] Disciplina Estrita: Corte distrações. Um foco monástico traz os melhores resultados.",
            "[Poder Água] Poder Silencioso: Você não precisa falar para ser ouvido. Sua presença é suficiente.",
            "[Alicerce Terra] Construindo Legado: Pensar a longo prazo rende frutos. Invista no seu futuro eu.",
            "[Vibe Cósmica] Alinhamento Estelar: A sorte vem de lugares inesperados. Mantenha-se aberto.",
            "[Ramo Madeira] Estendendo Limites: Saia da sua zona de conforto. O crescimento ocorre nas bordas.",
            "[Lareira de Fogo] Calor Compartilhado: Foco em equipe e comunidade. Juntos são mais fortes.",
            "[Espelho Metal] Autorreflexão: Olhe-se claramente. Avaliação honesta leva ao crescimento rápido.",
            "[Névoa Água] Mistério Creativo: Perfeito para pensamento não linear. Arte e música são seus guias.",
            "[Montanha Terra] Rocha Sólida: Pessoas te buscam por estabilidade. Ofereça liderança e calma.",
            "[Protagonista] Plot Armor: Não importa o obstáculo, você encontra o caminho. É a sua história!",
            "[Broto Madeira] Começo Suave: Cultiva pequenas ideias. Serão árvores gigantes em breve.",
            "[Faísca Fogo] Insight Inicial: Um momento 'Aha!' repentino. Anote-o imediatamente.",
            "[Minério Metal] Potencial Oculto: É necessário trabalho duro para revelar o diamante interior.",
            "[Riacho Água] Movimento Constante: Mantenha-se ativo. Estagnação é o único inimigo.",
            "[Campo Terra] Fertilidade: Tudo o que você plantar crescerá. Inicie um novo hábito ou skill.",
            "[Mestre Vibe] Vitória Aesthetic: Seu senso de estilo está no pico. Influencie naturalmente.",
            "[Folha Madeira] Mudança Visível: Resultados de esforços passados aparecendo. Aproveite a vista.",
            "[Raio Fogo] Impacto Directo: Suas palavras têm poder. Use-as para motivar e liderar.",
            "[Escudo Metal] Mente Resiliente: Nada abala sua determinação. Mantenha o foco.",
            "[Poço Água] Recurso Infinito: Você tem mais energia do que imagina. Deep dive nas tarefas.",
            "[Pedra Terra] Sucesso Durável: Uma vitória que dura. Estabilidade é seu novo status.",
            "[Final Boss] Imparável: Você superou todos os desafios. Agora, reivindique seu trono!"
        ],
        "LOVE_STYLES": [
            "Vibe de raposa astuta. Memoriza todo o seu lore.",
            "Energia de Golden Retriever! Lealdade lendária.",
            "Tsundere total. Frio com o mundo, fofo com você.",
            "Green flag absoluta. Prefere calls madrugadeiras.",
            "Modo gato selvagem. Respeite o espaço deles."
        ],
        "ELEMENT_SYNERGY": {
            "생": "[Duo Supremo] Uma sinergia incrível que preenche a alma um do outro.",
            "극": "[Química Picante] Diferentes, mas é por isso que se atraem tanto.",
            "비화": "[Vibe de Besties] Almas gêmeas que se entendem sem palavras."
        },
        "TIPS": [
            "Ser direto é o hack!",
            "Encontro surpresa para o hit de dopamina!",
            "Hype infinito pro crush!",
            "Vibe independente é tudo!",
            "Presentes específicos que eles amam!"
        ],
        "UI_STRINGS": {
            "profile": "👤 Perfil",
            "mbti_unrevealed": "Oculto / Enigmático",
            "signature": "🔮 [Sua Vibe Central]",
            "potential": "💫 [Lore Oculto & Poder]",
            "stage": "💼 [Onde você arrasa mais]",
            "guide": "🚀 [Guia do Glow-Up 2026]",
            "idol_mbti_fallback": "A saber (Vibe conectada via '{trait_name}')",
            "idol_mbti_fallback_random": "A saber (O destino os uniu)",
            "pure_saju_label": "🌟 Ressonância da Alma (Sem MBTI)",
            "mbti": "MBTI",
            "selectType": "Selecionar tipo",
            "female": "Feminino",
            "male": "Masculino",
            "nonbinary": "Não binário",
            "friendInfoTitle": "INFO DE AMIGO / PARCEIRO",
            "friendBirthLabel": "Data de Nascimento do Amigo",
            "friendGenderLabel": "Gênero do Amigo",
            "runAnalysis": "Analisar Resultado",
            "birthDatePrompt": "Por favor, insira sua data de nascimento primeiro para resultados precisos!",
            "mbtiPrompt": "Selecionar seu MBTI permite uma análise mais detalhada!",
            "error_msg": "Que cringe, o sistema Saju falhou. Tente de novo.",
            "organ_map": {"Wood": "Fígado/Vesícula", "Fire": "Coração/ID", "Earth": "Estômago/Baço", "Metal": "Pulmão/IG", "Water": "Rim/Bexiga"},
            "body_part_map": {"Wood": "Músculos/Olhos", "Fire": "Vasos/Língua", "Earth": "Pele/Boca", "Metal": "Vias/Nariz", "Water": "Ossos/Ouvidos"},
            "exercise_map": {"Wood": "Caminhada/Pilates", "Fire": "HIIT/Dança", "Earth": "Trilha/Musculação", "Metal": "Yoga/Boxe", "Water": "Natação/Meditação"},
            "luck_item_map": {"Wood": "Madeira/Verde", "Fire": "Vermelho/Sol", "Earth": "Amarelo/Terra", "Metal": "Branco/Metal", "Water": "Preto/Água"},
            "star_map": {"Wood": "Árvore", "Fire": "Sol", "Earth": "Terra", "Metal": "Diamante", "Water": "Oceano"},
            "skill_map": {"Wood": "Planejamento", "Fire": "Discurso", "Earth": "Coordenação", "Metal": "Análise", "Water": "Intuição"},
            "element_labels": {"Wood": "Madeira", "Fire": "Fogo", "Earth": "Terra", "Metal": "Metal", "Water": "Água"},
            "trait_map": {"Wood": "Vitalidade", "Fire": "Paixão", "Earth": "Tolerância", "Metal": "Decisão", "Water": "Sabedoria"},
            "place_map": {"Wood": "Parque", "Fire": "Palco", "Earth": "Café", "Metal": "Livraria", "Water": "Beira-rio"},
            "season_map": {"Wood": "Primavera", "Fire": "Verão", "Earth": "Mudança de Estação", "Metal": "Outono", "Water": "Inverno"},
            "flower_map": {"Wood": "Broto", "Fire": "Flor", "Earth": "Fruto", "Metal": "Semente", "Water": "Raiz"},
            "industry_map": {"Wood": "Arte/Criativo", "Fire": "IT/Mídia", "Earth": "Finanças/Imóveis", "Metal": "Tecno/Fab", "Water": "Serviço/Logística"},
            "style_map": {"Wood": "Puro", "Fire": "Chamativo", "Earth": "Estável", "Metal": "Chic", "Water": "Místico"},
            "mission_map": {"Wood": "Novo Desafio", "Fire": "Expressão", "Earth": "Equilíbrio", "Metal": "Melhoria", "Water": "Reflexão Interna"},
            "scientific_analysis": "🧬 [Análise de Dados Científicos Next-Gen]",
            "element_weight": "Pesos de Energia dos Elementos (Proporção 100%)",
            "mbti_dynamic": "Dinâmica Psicológica de Quatro Letras MBTI",
            "rpre_hypothesis": "Hipótese de Persona (Motor RPRE)",
            "REL_LABELS": {
                "A": "Duo Fantástico", "B": "Parceiro Estável", "C": "Companheiro de Esforço", "D": "Combo Único", "E": "Par de Novo Desafio"
            },
            "MBTI_TRAITS": {
                "E": "Extrovertido", "I": "Introvertido", "S": "Realista", "N": "Intuitivo",
                "T": "Lógico", "F": "Sensível", "J": "Planejado", "P": "Espontâneo"
            },
            "SYNERGY_LABELS": {
                "생": "Sinergia", "극": "Conflito", "조화": "Harmonia"
            },
            "MISSION_POINTS": ["charme", "especial", "twist", "de apaixonar", "ponto stan"],
            "month_names": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
            "stage_label": "ETAPA"
        },
        "MBTI_FUNC_FRAGMENTS": {
            "e_i": {
                "E": "tende a irradiar energia para fora e prosperar através da interação social,",
                "I": "foca a energia interna para criar resultados profundos e significativos,"
            },
            "n_s": {
                "N": "acredita na intuição e nas possibilidades futuras para trilhar caminhos criativos,",
                "S": "completa palcos perfeitos baseados em dados realistas e sensoriais,"
            },
            "t_f": {
                "T": "toma decisões lógicas e objetivas para estabelecer estratégias ideais,",
                "F": "toca corações através de uma empatia calorosa e troca emocional,"
            },
            "j_p": {
                "J": "proporciona confiança consistente com uma autogestão sistemática e planejada,",
                "P": "desfruta de mudanças flexíveis e espontâneas, mostrando um charme radiante em qualquer lugar."
            }
        },
        "RPRE_TEMPLATES": {
            "core_v1": "Sobre a poderosa essência de {p1}, acrescenta-se o sentido sofisticado de {p2}. Embora a estrela vista a persona de {mbti} e apareça como tal para o público, em momentos críticos, a persistência inerente de {p1} transparece, revelando um estilo de 'Mão de ferro em luva de veludo'.",
            "hero_v2": "A base cósmica de {p1} fornece um alicerce sólido para a centelha criativa de {p2}. Conhecida publicamente como o ícone {mbti}, a verdadeira força da estrela reside em uma frequência '{element}' oculta que só emerge sob pressão.",
            "mystic_v3": "Guiada pela intuição de {p1} e refinada pela execução de {p2}, a persona de {mbti} atua como uma bela máscara. Por trás dela, opera um complexo motor de equilíbrio elemental, criando um campo magnético irresistível."
        },
        "MZ_ANALYSIS_FRAGMENTS": {
            "action_guides": {
                "vibe": [
                    "Monte uma playlist com as músicas favoritas de {idol} e poste nas redes com seu toque MZ.",
                    "Visite um lugar que {idol} foi recentemente e recrie a pose deles — missão peregrinação completa.",
                    "Encontre o gosto em comum e mande pra {idol} aquele sinal de 'isso aí somos demais nós'.",
                    "Crie um look com a cor pessoal de {idol} ou suas peças favoritas. Era sósias ativada.",
                    "Escreva com caligrafia uma frase da entrevista de {idol} que te arrasou e poste pro fandom ver.",
                    "Leia ou assista algo que {idol} mencionou e solte a sua resenha MZ-style na timeline."
                ],
                "heart": [
                    "Lembre daquele hábito miudinho de {idol} e traga no fan meet ou app de fãs. Que sinta que você vê de verdade.",
                    "Escreva de próprio punho uma carta ou mensagem usando palavras que elevem a força interior de {idol}. Sério mesmo.",
                    "Entenda a diferença T/F dos MBTIs de vocês e prepare as palavras exatas que {idol} precisa ouvir quando balançar.",
                    "Reuna as frases que dão força a {idol} e embale como um presente de 'playlist de incentivo'.",
                    "Planeje uma comemoração simples e sincera não só no aniversário mas também no aniversário de estreia de {idol}.",
                    "Edite um clip com todos os momentos que você viu {idol} crescer — manda com amor genuino e só."
                ],
                "energy": [
                    "Organize um trabalho voluntário com impacto ou projeto de fãs na data de aniversário de {idol}.",
                    "Monte merch ou outfit com a cor pessoal de {idol} pra somar hype no fandom.",
                    "Aprenda o hobby que {idol} começou recentemente, em espírito fazem juntos. Nova era, novo desafio.",
                    "Crie seu próprio vídeo de challenge com a música de {idol} e espalhe energia positiva pra geral.",
                    "Começe o exercício que {idol} pratica, registre seu progresso e compartilhe essa energia com o universo.",
                    "Deixe uma mensagem matinal vibrante e quentinha no canal de fãs de {idol} todo dia. Seja o solzinho deles."
                ]
            },
            "relationship_intro": [
                "Sua frequência sincroniza em {score}%! Um combo de {rel_label}.",
                "Sinais cósmicos atingindo forte nesta química de {rel_label}.",
                "Basicamente destino, esta vibe de {rel_label} é inegável.",
                "Dados provam que este match de {rel_label} é elite, pontuação {score}!",
                "Ressonância entre suas ondas cria uma obra-prima de {rel_label}.",
                "Um timing de {rel_label} através do tempo e espaço, {score}% de probabilidade."
            ],
            "relationship_core": [
                "Uma relação de livro didático perfeita onde preenchem os vazios um do outro.",
                "Uma narrativa de tensão e crescimento, como um drama juvenil de superação.",
                "Um duo invencível que parece ter o mundo inteiro aos seus pés.",
                "As diferenças atuam como um catalisador para o crescimento e a emoção mútua.",
                "Sincronização de almas onde um único olhar diz tudo.",
                "Um combo de poder positivo que pode superar qualquer obstáculo com um sorriso."
            ],
            "bias_essence": [
                "Tem uma forte energia '{element}', exalando uma aura carismática.",
                "O traço dominante de '{element}' mistura sensibilidade com domínio de palco.",
                "Como um sol quente, é uma vitamina humana irradiando energia positiva.",
                "Sólido como uma rocha, um ícone de 'Green Flag' que oferece confiança constante.",
                "Flexível como água límpida, possuindo um charme profundo e misterioso.",
                "A força do metal e o brilho de uma gema, brilhando com o passar do tempo."
            ],
            "bias_point": [
                "A maior atração é o abismo entre o carisma e as vibes de cachorrinho.",
                "Fãs amam a mistura de 'Modo Pro' e momentos de TMI diário inesperados.",
                "Um observador silencioso cujas raras palavras explodem com alta dopamina.",
                "O amor delicado pelos fãs e o compartilhamento de pequenos momentos rouba corações.",
                "A confiança vem de sua constante melhoria pessoal e crescimento visível.",
                "Senso visual inigualável e estética única em cada visual."
            ],
            "bias_tmi": [
                "Sendo {mbti}, literalmente vive aquela vida de deus ultra organizada — esse personão planeja tudo enquanto a gente ainda tá no modo vibe.",
                "Com essa energia icônica de {mbti}, lembra até da reação mais mínima do fã — aquele tweet de 3 meses atrás? Viu sim. Lembra sim.",
                "Essa personalidade {mbti} significa que precisa de tempo a sós pra recarregar — gato certificado com energia de protagonista independente.",
                "Puro caos {mbti} mas do bom: sempre cozinhando ideias criativas que deixam os fãs em choque toda vez. Total ideia bank.",
                "Por fora parece calmo, mas aquele quirk inesperado de {mbti} bate diferente — VAI quebrar o silêncio com algo loucamente icônico.",
                "Essa energia {mbti_trait} é muito real — sem querer vira o terapeuta do grupo e todo mundo confia naturalmente nele tudo."
            ],
            "recent_fortune": [
                "{idol} está no modo comeback total. Career high entrando — as estrelas literalmente se alinharam pra esse momento, sem mentira.",
                "A sorte de interação tá SUBINDO. Uma reação legendária, um momento icônico com o fandom — vem aí e vai ficar na TL pra sempre.",
                "Esse é um arco de recarga, mas não se engane — a aura tá ficando MAIS PROFUNDA. Quando voltar, vai ser uma era de arrasa no outono.",
                "Um apoio major na carreira acabou de entrar em órbita. Uma collab global inesperada? O saju diz que não é SE, é QUANDO.",
                "A era financeira e de marca de {idol} tá batendo diferente. Contratos, projetos solos — garantindo o bag. Stan queen/king do negócio.",
                "A paixão interna tá NO PICO MÁXIMO. O que quer que {idol} tenha criado por conta própria tá prestes a cair e NÃO vai passar em branco."
            ],
            "synergy_why": [
                "A energia do seu '{u_element}' com a do(a) {idol} ('{i_element}') é uma química de milhões — o choque tá entregando tudo! ✨",
                "Os mapas Saju de vocês se completam perfeitamente e zeram as fraquezas. Juntos, a sorte de vocês simplesmente destrava. Match de milhões! 💖",
                "O combo de {u_mbti} e {i_mbti} cobre os pontos cegos um do outro com precisão assustadora. O duo mais equilibrado do chart, fr.",
                "'{u_element}' alimentando a energia '{i_element}' é basicamente uma dinâmica de apoio perfeita — você é genuinamente a fonte de poder deles.",
                "'{u_element}' e '{i_element}' são sabores diferentes que de alguma forma criam uma química viciante. O rizz é mútuo e não tem igual.",
                "O impulso de {u_mbti} mais a natureza detalhista de {i_mbti}? Juntos são literalmente imparáveis. Duo de final boss."
            ]
        },
        "PURE_LOVE_STYLES": [
            "Um tipo de cavalo selvagem que acredita em atrações intuitivas e avança com ousadia.",
            "Um vínculo profundo e estável, como se estivesse conectado desde uma vida passada.",
            "Uma chave para a alma que preenche magicamente as partes que faltam."
        ],
        "PURE_SYNERGY": {
            "생": "[Duo Supremo] Uma sinergia incrível que preenche a alma um do outro.",
            "극": "[Química Picante] Diferentes, mas é por isso que se atraem tanto.",
            "비화": "[Vibe de Besties] Almas gêmeas que se entendem sem palavras."
        },
        "PURE_TIPS": [
            "Mostre o charme natural do seu elemento sem falsidade para ser mais poderoso.",
            "Caminhar juntos na natureza fará a sincronização explodir.",
            "Acreditar na essência um do outro, mesmo no silêncio, é a resposta certa."
        ],
        "TIP_COMPONENTS": {
            "actions": [
                "Com a honestidade autêntica de {mbti}, sem jogar mind games",
                "Canalizando a energia mútua de {u_el} pra elevar um ao outro",
                "Planejando um evento surpresa inesperado em {place}",
                "Respeitando cada traço pequenininho de {mbti_trait} — é aí que a magia acontece",
                "Curtindo sessões só de vocês dois de {exercise}",
                "Sincronizando a vibe quando a energia de {star} tá no pico",
                "Soltando um humor {mbti}-coded inesperado de vez em quando",
                "Mantendo aquela aura clássica e estável de {mbti_trait} que te define",
                "Chegando com o {luck_item} favorito do star — mó hype",
                "Mostrando seu {skill} de nível pro pra ele/ela notar",
                "Sendo o/a dono/a das reações genuínas — essa é sua vibra",
                "Priorizando cuidar de {organ} primeiro — saúde é o verdadeiro glow-up",
                "Fazendo uma peregrinação juntos pelos lugares sagrados de {place}",
                "Escrevendo uma carta de coração celebrando o {trait} do star",
                "Mantendo aquela vibe cool única de {mbti} que te faz icônico/a"
            ],
            "topics": [
                "elogiar a energia magnética de {trait} do star",
                "aproveitar a sinergia elemental {u_el}/{i_el} que une vocês",
                "se preocupar primeiro com o bem-estar de {organ} do star",
                "ativar o poder do {luck_item} mais querido pelo star",
                "trocar conselhos genuínos e reflexivos sobre {skill}",
                "propor um tour juntos por {place}",
                "compartilhando as leituras de fortuna de {star} entre vocês",
                "hypeando o lado {mbti_trait} do star — ele/ela precisa ouvir isso",
                "mencionando aquela palavra-chave de {trait} de uma entrevista antiga",
                "spilando tudo sobre a obsessão #1 do star com {luck_item}",
                "propondo um challenge de {exercise} em dupla",
                "presenteando com um item de cor da sorte que conecta com a energia {u_el} do star"
            ],
            "results": [
                "o cheat code definitivo pra inundar o relacionamento de dopamina.",
                "o segredo pra sincronizar as almas de vocês na mesma frequência.",
                "o caminho pra plantar uma green flag inabalável de certeza.",
                "o movimento que fortalece o fio do destino que existe desde vidas passadas.",
                "o atalho mais rápido pra se tornar a pessoa #1 na vida dele/dela.",
                "a peça final que completa a química exclusiva de vocês.",
                "a forma de criar uma sinergia de nível god que acelera o coração.",
                "o método pra virar personagens principais do destino um do outro.",
                "o sinal definitivo que responde ao opening line não dito do star.",
                "a estratégia pra amplificar a sinergia de {rel_type} em 200%."
            ]
        },
        "GEN_MISSION_COMPONENTS": {
            "actions": {
                "E": [
                    "Panfletando as fotos de {target} na comunidade", "Divulgando o charme {trait} do star pros besties", 
                    "Participando de uma trend no TikTok/Twitter", "Fazendo live num {place} icônico que ele foi",
                    "Criando e espalhando memes bem {mbti} dele", "Fazendo um desafio de {exercise} junto com o fandom",
                    "Indo tirar foto no anúncio de aniversário do star", "Dando ideias pra fazer merch em grupo",
                    "Gravando você gritando o fanchant do comeback", "Surtando junto imaginando uma interação {point} com ele"
                ],
                "I": [
                    "Fazendo um polco (journal) tranquilamente com {target}", "Fazendo maratona das fancams {trait} do passado",
                    "Passando um tempo sozinho no {place} que o star citou", "Meditando com a playlist do star",
                    "Escrevendo uma cartinha cheia de sentimentos pra ele", "Guardando em segredo o {luck_item} do star",
                    "Mantendo um diário privado das vibes {mbti} dele", "Assistindo fancam no repeat em casa",
                    "Analisando o mapa {star} dele como amuleto da sorte", "Escrevendo as palavras de conforto que ele disse"
                ]
            },
            "targets": {
                "Wood": ["merch com tema de plantinhas verde", "local de peregrinação com cheiro de floresta", "vídeo da era de crescimento dele", "lucky item verde"],
                "Fire": ["item vermelho bem chamativo", "fancam fiery do palco", "local com uma vista noturna deslumbrante", "cena de paixão pura"],
                "Earth": ["merch bege bem aesthetic", "lugar calmo com vibe earthy", "foto do dia a dia do star", "registro do esforço silencioso dele"],
                "Metal": ["acessório prateado chic", "photoshoot com carisma afiado", "lugar com design minimalista", "entrevista mostrando a força de vontade dele"],
                "Water": ["photocard com vibe de oceano azul", "rádio relaxante com som de chuva", "música lenta profunda", "item com vibe transparente e clara"]
            },
            "contexts": [
                "Amplifique a sinergia de {rel_type} em 200%!", "Aproveite o momento em que as frequências de vocês se alinham.",
                "Fortaleça ainda mais o fio vermelho da vida passada.", "O atalho mais rápido pra virar o #1 no coração dele.",
                "Complete a sua green flag suprema.", "Sincronize sua energia com a vibe {u_el} do star.",
                "A última peça pro quebra-cabeça da química secreta de vocês.", "Experimente aquela sinergia god-tier que faz o coração acelerar.",
                "Se torne o bestie definitivo.", "A mágica pra transformar as diferenças num charme {point}."
            ]
        },
        "MISSION_COMPONENTS": {
            "labels": [
                "Missão Fase {n}: {u_mbti} x {i_mbti}",
                "Fusão de Energia {u_el} & {i_el}",
                "Escapar da Era de Negação Stan: {point}",
                "Ativar o Buff de Protagonista: {point}",
                "Sincronização de Frequência do Destino",
                "Guia de Estratégia {i_mbti} Personalizada",
                "Quebrar o Teto da Química: {point}",
                "Foto Prova da Alma Gêmea",
                "Missão Carga Total de Dopamina",
                "Rotina de Sinergia God-Tier",
                "Escapar do Estacionamento de Vidas Passadas: {point}",
                "Desbloquear o Campo de Força de {trait} do Star",
                "Caminhar Juntos pelo Caminho de {rel_type}"
            ],
            "reasons": [
                "No K-saju, {u_el} cria e sustenta {i_el} — esse é o blueprint do destino de vocês.",
                "A energia {mbti_trait} de {u_mbti} é um estímulo fresco que o star precisa.",
                "Isso repara o ponto de tensão onde as energias de {organ} se chocam.",
                "É a solução pra corrigir o pequeno desalinhamento do mapa de vidas passadas.",
                "A energia {star} do star tá em ressonância com sua frequência {u_el} agora mesmo.",
                "Isso eleva a sinergia de {rel_type} entre vocês ao nível absoluto máximo.",
                "A vibe {mbti} do star tá lowkey obcecada com sua energia {mbti_trait}."
            ],
            "tasks": {
                "vibe": [
                    "Criar merch personalizada centrada no {trait} icônico do star",
                    "Decorar seu diário com fotocards que mostram a compatibilidade {mbti} de vocês",
                    "Recriar uma foto em {place} que o star mencionou, na mesma pose exata",
                    "Aprender de verdade o {skill} que o star tá obcecado agora",
                    "Postar com um {luck_item} que bate com a paleta de cor pessoal do star",
                    "Escrever a frase mais icônica do star em caligrafia e compartilhar",
                    "Streamear {n} vezes o novo palco do star e postar prova",
                    "Criar um meme viral sobre os momentos cotidianos {mbti}-coded do star"
                ],
                "heart": [
                    "Fazer tag em massa na hashtag da SNS pra apoiar a saúde de {organ} do star",
                    "Mandar uma mensagem de apoio genuinamente {mbti_trait} e do coração",
                    "Presentear com um item parecido com o {luck_item} que o star mais ama",
                    "Escrever uma caligrafia exaltando a aura de {star} do star",
                    "Assistir em maratona os vídeos da era debut do star sobre {trait}",
                    "Mandar exatamente as palavras calorosas de conforto que o star merece ouvir",
                    "Escrever uma carta à mão analisando a personalidade {mbti} do star e postar",
                    "Se dar um momento de autoapreciação por apoiar pacientemente o crescimento do star"
                ],
                "energy": [
                    "Postar prova do treino com a mentalidade de fazer {exercise} junto ao star",
                    "Se vestir com uma cor da sorte alinhada à energia {i_el} do star",
                    "Editar um vídeo de {n} minutos que capture a narrativa épica do star",
                    "Confiar na sinergia {u_el}/{i_el} e aceitar um novo desafio pessoal",
                    "Meditar com a playlist do star e limpar seu campo de energia",
                    "Viver sua melhor vida como o star faria — anotar e compartilhar prova",
                    "Exibir o outfit do dia com o item de sorte de {star} do star",
                    "Falar pra pelo menos uma pessoa hoje sobre a magia de {trait} do star"
                ]
            }
        },
        "SYNERGY_MISSIONS": {
            "analysis_1": {
                "label": "Compartilhar Vibes: {point_1} 📸",
                "boost": 15,
                "reason": "Análise profunda de gostos baseada em {reason_1}.",
                "tasks": ["{task_1_1}", "{task_1_2}", "{task_1_3}"]
            },
            "analysis_2": {
                "label": "Soul Sync: {point_2} 💬",
                "boost": 15,
                "reason": "Ressonância espiritual através de {reason_2}.",
                "tasks": ["{task_2_1}", "{task_2_2}", "{task_2_3}"]
            },
            "analysis_3": {
                "label": "Ação Cósmica: {point_3} 🎡",
                "boost": 20,
                "reason": "Atividades de cura para {reason_3}.",
                "tasks": ["{task_3_1}", "{task_3_2}", "{task_3_3}"]
            }
        },
        "EXPERT_ADVICE": {
            "Health": [
                "Agente A (Tradicional): Seu elemento sugere uma fraqueza na área de {organ}. O Saju tradicional recomenda chás de ervas para equilibrar sua energia interna.",
                "Agente B (Psicológico): O estresse tende a se manifestar em seu {body_part}. Priorize momentos de calma e meditação profunda para evitar o esgotamento.",
                "Agente C (Tendência): Experimente {exercise}, tendência em Seul. É o fluxo perfeito para circular seu tipo de energia específica."
            ],
            "Wealth": [
                "Agente A (Legado): Um forte alinhamento financeiro ocorre no mês {month}. Esta é sua oportunidade para investimentos de longo prazo.",
                "Agente B (Comportamental): Você tende a gastar impulsivamente quando sua energia está alta. Estabeleça uma 'Regra de Espera' para compras grandes.",
                "Agente C (Tech): Usar um acessório com o tema de {luck_item} funcionará como um ímã de sorte para sua renda secundária."
            ],
            "Career": [
                "Agente A (Autoridade): Sua carta mostra a energia de 'A {star}'. Você é um líder nato destinado à alta gerência.",
                "Agente B (Social): Seu estilo de networking é sua arma mais afiada. Foque no 'Poder Suave' para conquistar colegas difíceis.",
                "Agente C (Skill): Melhorar em {skill} é seu código secreto para 2026. Esta sinergia ativará uma mudança massiva em sua carreira."
            ],
            "Love": [
                "Agente A (Destiny): Você tem uma conexão predestinada com alguém com energia de '{element}'. Eles são a peça que falta.",
                "Agente B (Aura): Seu maior encanto é seu '{trait}'. Use isso em seus encontros; é o que te torna inesquecível.",
                "Agente C (Vibe): Prevê-se um encontro de alta probabilidade em um {place}. Mantenha sua energia de protagonista ao visitar."
            ]
        },
        "LIFETIME_EXPERTS": [
            {
                "name": "Mestre Cheong",
                "focus": "Ciclo Maior e Equilíbrio Elemental",
                "comment": "Seu destino flui com a energia de {season}. Como um grande rio, você superará os obstáculos e alcançará seu sucesso na segunda metade da vida."
            },
            {
                "name": "Dra. Jung",
                "focus": "Temperamento Interno e Fluxo Emocional",
                "comment": "Você tem a alma delicada de uma {flower}. Nunca duvide de sua frequência única; sua sensibilidade é, na verdade, seu maior poder."
            },
            {
                "name": "Neo",
                "focus": "Aptidão Tecnológica e Lógica de Riqueza",
                "comment": "Seu algoritmo de energia está otimizado para o setor de {industry}. Você possui o olho analítico para identificar riqueza oculta."
            },
            {
                "name": "Sophie",
                "focus": "Profundidade de Relacionamento e Ressonância",
                "comment": "No amor, você transmite vibes de '{style}'. Pode ser difícil expressar sentimentos, mas uma vez comprometido, você é um parceiro lendário."
            },
            {
                "name": "Mestre Zen",
                "focus": "Missão de Vida e Alinhamento Holístico",
                "comment": "Sua missão final não é apenas o sucesso, mas '{mission}'. Sua aura clara guiará naturalmente os outros e criará um efeito positivo."
            }
        ],
        "MZ_SAJU_DICTIONARY": {
            "일주": "A energia do dia em que você nasceu! A vibe central e sua verdadeira essência.",
            "용신": "Seu amuleto da sorte. Estimular essa energia deixa a vida muito mais fácil!",
            "기구신": "A energia 'vilã' sutil. Domine-a para proteger sua paz mental.",
            "상생": "Apoio mútuo e vibe de melhores amigos. A definição de 'nós combinamos muito'.",
            "상극": "Química intensa onde o atrito gera um crescimento estrondoso.",
            "도화살": "Energia de personagem principal. Uma aura natural que atrai olhares facilmente.",
            "역마살": "Vibe de viajante global. Não consegue ficar parado; fluir atrai a grande sorte.",
            "현침살": "O mestre dos 'fatos'. Percepção extrema e amor pelos mínimos detalhes.",
            "비견": "Dinâmica de colega alma gêmea. Aumenta seu squad de amigos confiáveis.",
            "겁재": "Instinto competitivo. Uma leve rivalidade te faz crescer na velocidade da luz!",
            "편인": "O excêntrico 'banco de ideias'. Pensar fora da caixa é o seu grande charme.",
            "정인": "Nascido para ser amado. A vibe de caçula que todo mundo enche de mimos.",
            "식신": "Cheio de talento e com sorte para a comida. Produtivo e sabe curtir a vida como ninguém.",
            "상관": "Inovador rebelde. Quebra os padrões e detesta rótulos—caos puramente criativo!",
            "편재": "Jackpot inesperado. Adora arriscar alto atrás daquele sucesso monumental.",
            "정재": "O seguro e confiável 'livro caixa humano'. Constrói a vida passo a passo.",
            "편관": "Líder carismático temperado pelas dificuldades. Risco alto, recompensa lendária.",
            "정관": "O aluno nota 10 certinho. Vibra princípios fortes e segue um caminho sólido."
        }
    }
}

def get_localized_data(lang: str) -> Dict[str, Any]:
    return I18N_DATA.get(lang, I18N_DATA.get('ko'))
