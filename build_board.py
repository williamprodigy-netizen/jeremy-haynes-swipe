#!/usr/bin/env python3
"""Jeremy Haynes — The Backend Blueprint, the whole funnel, wired.

One pannable canvas. Every funnel step is the real captured page.

Layout rule: one column per funnel STEP. Parallel variants stack vertically
inside that column so an arrow never crosses a card it is not pointing at.

Run:  python3 build_board.py   ->  board.html
"""
import os, sys, glob

sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
import boardbuild

HERE = os.path.dirname(os.path.abspath(__file__))
EV = os.path.expanduser(
    "~/UNDERGROUND_FUNNELS_SSOT/01_RAW_FUNNELS/"
    "Jeremy_Haynes_Megalodon_Marketing - The_Backend_Blueprint_free_live_class_-_Master_Int - 2026-08-11"
    "/02_Pages")


def png(folder):
    hits = sorted(glob.glob(os.path.join(EV, folder, "*screenshot_fullpage.png")))
    if not hits:
        raise SystemExit(f"no capture for {folder}")
    return hits[0]


SHOTS = {
    # ------------------------------------------- LANE 1 · the free class funnel
    "reg": dict(col=1, y=170, lane="paid", step="STEP 1 · OPT-IN",
                img=png("01_Webinar_registration"), max_h=1500,
                title="Registration — The Backend Blueprint",
                url="jeremysworkshops.com/",
                note="Free live class, Wednesday April 8th 7:00 PM EST, live on Zoom. "
                     "Countdown timer, one testimonial, then the form. Four fields "
                     "plus an SMS consent box. Built on bolt.new. "
                     "<b>Still live today with the countdown at 00:00:00:00.</b>"),
    "ty": dict(col=2, y=170, lane="paid", step="STEP 2 · CONFIRMATION",
               img=png("02_Thank-you_page"), max_h=1400,
               title="Confirmation — &ldquo;You're In!&rdquo;",
               url="jeremysworkshops.com/confirmation",
               note="A 8m58s Wistia video at the top, then exactly two homework "
                    "items: whitelist the sender, and go watch him on YouTube. "
                    "This page is the thing he spends the first 15 minutes of the "
                    "class teaching."),
    "replay": dict(col=3, y=170, lane="ever", step="STEP 3 · REPLAY + PITCH",
                   img=png("03_Replay_page"), max_h=1500,
                   title="Replay page — the whole pitch in text",
                   url="jeremysworkshops.com/replay",
                   note="The 1h26m class replay, then the Master Internet Marketing "
                        "pitch written out below it: 7 weeks live, video library, "
                        "private community, certification. <b>No price anywhere on "
                        "the page.</b> Both CTAs go to a calendar."),
    "cal": dict(col=4, y=170, lane="back", step="STEP 4 · CALL",
                img=png("09_Calendar_OnceHub"), max_h=900,
                title="Calendar — OnceHub, 30 minutes",
                url="go.oncehub.com/MasterInternetMarkting",
                note="Not GHL, not Calendly. OnceHub, 30-minute slot, and the "
                     "booking page still carries the typo in the URL: "
                     "<code>MasterInternetMarkting</code>."),

    # ------------------------------------------------- LANE 2 · the other offer
    "bbs": dict(col=3, y=1900, lane="event", step="SEPARATE OFFER",
                img=png("04_Application"), max_h=1500,
                title="Business Breakthrough Session — $2,000, in person",
                url="jeremysworkshops.com/breakthroughsession",
                note="Same domain, different business. $2,000 one-time to fly to "
                     "Miami and sit in his office for 60&ndash;90 minutes. "
                     "$200K/mo minimum to qualify. He films it for the channel, "
                     "which is why the price is low &mdash; the session pays for "
                     "itself as content."),
    "tf": dict(col=4, y=1900, lane="event", step="APPLICATION",
               img=png("08_Application_form_Typeform"), max_h=900,
               title="Typeform application — 5 questions",
               url="ahbigalex10.typeform.com/to/xNGN4m10",
               note="Name, MRR band, Instagram handle, have-you-watched-the-YouTube, "
                    "contact. The IG handle is the verification lever: they eyeball "
                    "the account against the MRR claim."),
    "bbty": dict(col=5, y=1900, lane="event", step="APPLICATION TY",
                 img=png("05_Application_thank-you"), max_h=800,
                 title="Application confirmation",
                 url="jeremysworkshops.com/bbconfirmation",
                 note="Typeform redirects here on submit. Thin page &mdash; the real "
                      "next step is a human texting you to verify the $200K claim."),
}

DATA = {
    "traffic": dict(col=1, y=1900, lane="paid", step="ENTRY",
                    title="Paid Meta — 3 creatives, 38 days",
                    url="facebook.com/ads/library/?view_all_page_id=234697063572758",
                    kv=[("Page ID", "234697063572758"),
                        ("Flight", "Apr 5 &rarr; May 11 2026"),
                        ("Creatives", "3 cuts, one script"),
                        ("Hook", "&ldquo;Your Show Rates Are Down&rdquo;"),
                        ("Placements", "FB / IG / Messenger / Threads"),
                        ("Status now", "zero active ads")],
                    note="One flight, then dark. Ad IDs 751659421234740, "
                         "1967551464135245, 1990698711832620."),
    "stack": dict(col=2, y=1900, lane="paid", step="STACK",
                  title="What it is actually built on",
                  kv=[("Site", "bolt.new / React SPA"),
                      ("Video", "Wistia &times; 4"),
                      ("Pixel", "Meta 699008397340708"),
                      ("Form target", "Zapier catch hook"),
                      ("CRM", "none visible"),
                      ("Calendar", "OnceHub"),
                      ("Application", "Typeform")],
                  note="There is no funnel builder and no CRM form here. The opt-in "
                       "POSTs to <code>hooks.zapier.com/hooks/catch/3797197/uxc7bj5/</code> "
                       "and Zapier fans it out from there."),
    "close": dict(col=5, y=170, lane="back", step="THE CLOSE",
                  title="Two doors: Buy or Call",
                  kv=[("MIM price", "$5,000"),
                      ("Payment plans", "none, by policy"),
                      ("Length", "7 weeks live"),
                      ("Jeremy AI", "$300/mo or $2,000/yr"),
                      ("Close device", "two QR codes on screen"),
                      ("Guarantee", "none stated")],
                  note="The final slide is literally <b>Buy</b> and <b>Call</b> side "
                       "by side, each with its own QR code. Self-serve and "
                       "book-a-call are offered simultaneously, not sequentially."),
}

BRANCH = [
    dict(x=boardbuild.X[1], y=2560, state="ok",
         cond="Opt-in submitted",
         body="Form POSTs to a Zapier catch hook. No CRM write is observable from "
              "the client, so email/SMS delivery all happens inside Zapier.",
         ev="VERIFIED &mdash; endpoint read from the React bundle"),
    dict(x=boardbuild.X[2], y=2560, state="ok",
         cond="Registered, class not yet run",
         body="&ldquo;Value dense&rdquo; email sequence plus the Hammer Them SMS "
              "campaign run between opt-in and the class. He states the target is a "
              "50%+ open rate and gives the sequence away to anyone who stays to the end.",
         ev="EVIDENCE &mdash; described on-slide and in the replay, not observed in our inbox"),
    dict(x=boardbuild.X[3], y=2560, state="ok",
         cond="Did not show",
         body="A one-line survey email, subject &ldquo;feedback&rdquo;, asking why "
              "they did not show. The answers are fed back into the confirmation-page "
              "breakout videos.",
         ev="EVIDENCE &mdash; taught on-slide as his own system"),
    dict(x=boardbuild.X[4], y=2560, state="warn",
         cond="Watched the replay",
         body="Both replay-page CTAs go straight to the OnceHub calendar. There is "
              "no application, no qualification and no price between the video and "
              "the booking.",
         ev="VERIFIED &mdash; both CTAs captured"),
    dict(x=boardbuild.X[5], y=2560, state="warn",
         cond="$200K+/mo founder",
         body="Different lane entirely. Typeform gates on MRR, a human verifies by "
              "text, payment is taken, and only then is a scheduler link released.",
         ev="VERIFIED &mdash; the 5-step process is written on the page"),
]

LABELS = [
    dict(x=boardbuild.X[1], y=90, t="LANE 1 &middot; FREE LIVE CLASS &rarr; $5,000 MIM"),
    dict(x=boardbuild.X[1], y=1820, t="ENTRY, STACK &amp; THE SECOND OFFER"),
    dict(x=boardbuild.X[1], y=2490, t="ROUTING LOGIC"),
]

EDGES = [
    ("reg", "ty"), ("ty", "replay"), ("replay", "cal"), ("cal", "close"),
    ("traffic", "reg", "v", "#818cf8"),
    ("bbs", "tf"), ("tf", "bbty"),
]

boardbuild.build(dict(
    OUT=os.path.join(HERE, "board.html"),
    TITLE="Jeremy Haynes — The Backend Blueprint",
    KICK="UNDERGROUND FUNNELS · F131 · CAPTURED 11 AUG 2026",
    BLURB="A free live class that sells a $5,000 seven-week program, run once on "
          "paid Meta for 38 days and then left standing. Two offers share the "
          "domain. The whole thing is a bolt.new SPA wired to a Zapier hook.",
    SHOTS=SHOTS, DATA=DATA, BRANCH=BRANCH, LABELS=LABELS, EDGES=EDGES,
    HOME="index.html",
    LEGEND=[("paid", "Paid entry · free class"),
            ("ever", "Evergreen replay"),
            ("back", "Back end · $5,000 MIM"),
            ("event", "$2,000 in-person session")],
))
