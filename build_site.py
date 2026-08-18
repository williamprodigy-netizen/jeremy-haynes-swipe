#!/usr/bin/env python3
"""Build the Jeremy Haynes — Backend Blueprint swipe site.

Run: python3 build_site.py
"""
import sys, os, glob
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/JEREMY_HAYNES_Swipe")

CONFIG = {
    "SITE": "The Backend Blueprint — Jeremy Haynes / Megalodon Marketing",
    "CREATOR": "Jeremy Haynes",
    "ADS_KEY": "jeremy_haynes",
    "FUNNEL_IDS": ["F131"],
    "CAPTURED": "11 August 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/JEREMY_HAYNES_Swipe",
    "BLURB": "A free live class that sells a <b>$5,000</b> seven-week program with "
             "<b>no payment plans and no guarantee</b>. The entire teaching content is "
             "the thing we are currently worst at &mdash; getting registrants to actually "
             "show up. Run once on paid Meta for 38 days, then left standing with a dead "
             "countdown.",

    "PAGES": [
        ("index.html", "Overview"),
        ("analysis.html", "Analysis"),
        ("slides.html", "Slides"),
        ("transcripts.html", "Transcripts"),
        ("videos.html", "Video library"),
        ("board.html", "Funnel board"),
    ],

    "STATS": [
        ("MIM price", "$5,000"),
        ("Payment plans", "None"),
        ("Guarantee", "None"),
        ("Class length", "1h 26m"),
        ("Paid flight", "38 days"),
        ("Creatives", "3"),
        ("Slides pulled", "77"),
        ("2nd offer", "$2,000"),
    ],

    "OFFER": [
        ("Front end", "&ldquo;The Backend Blueprint&rdquo; &mdash; free live class, Zoom, "
                      "Wednesday April 8th 7:00 PM EST"),
        ("Back end", "Master Internet Marketing &mdash; 7 weeks live, <b>$5,000</b>, "
                     "lifetime access, certification"),
        ("Second offer", "Business Breakthrough Session &mdash; <b>$2,000</b>, in person in "
                         "Miami, 60&ndash;90 min, $200K/mo minimum to qualify"),
        ("Third offer", "Jeremy AI &mdash; $300/mo or $2,000/yr standalone"),
        ("Big idea", "&ldquo;It's not a you problem. It's a systems problem.&rdquo;"),
        ("Mechanism", "Five <b>backend selling systems</b>: confirmation pages, value-dense "
                      "email, the Hammer Them campaign, setter pre-call, AI manipulation"),
        ("Villain", "Your numbers moving the wrong way with no playbook &mdash; show rates "
                    "down, close rates shrinking, leads arriving needing funding"),
        ("Awareness", "Problem-aware operators who already run sales calls. He never "
                      "explains what a funnel is."),
        ("Entry", "First name, last name, email, <b>phone</b>, SMS consent checkbox"),
        ("Form target", "<code>hooks.zapier.com/hooks/catch/3797197/uxc7bj5/</code> &mdash; "
                        "a bare Zapier catch hook, no CRM"),
        ("Close", "Two QR codes on one slide: <b>Buy</b> and <b>Call</b>"),
        ("Entity", "Megalodon Marketing LLC, 1900 N Miami Ave, Miami FL 33136"),
    ],

    "FINDINGS": [
        ("The whole class is a show-rate class, and he charges $5,000 for it",
         "Every one of the five systems he teaches exists to move one number: the "
         "percentage of registered people who actually turn up. He opens with "
         "<i>&ldquo;we're going to help you improve your show rates&rdquo;</i> and closes 86 "
         "minutes later on a $5,000 program. This is the exact problem we are stuck on, "
         "taught by someone selling the fix at five grand a seat."),
        ("Urgency video first, information videos second &mdash; the order is the finding",
         "On a client's co-living funnel he put a single urgency video at the top of the "
         "confirmation page: 13 US cities had just legalised the model, first movers win. "
         "That one video moved the webinar show rate <b>19 points</b>. He then added "
         "<b>19</b> information &ldquo;breakout&rdquo; videos answering sales-team "
         "objections &mdash; those added only <b>4 points</b>. His conclusion: nobody cares "
         "about the information until you have given them a reason to care. "
         "<span class=\"tag warn\">His numbers, unaudited</span>"),
        ("He live-screenshares his Stripe dashboard as the trust proof",
         "The 8m58s confirmation-page video is not a &ldquo;lock it in your calendar&rdquo; "
         "video. He opens Stripe on screen, scrolls it live so you can see it is not a "
         "screenshot, and shows a <b>0.37% lifetime dispute rate across 7,241 "
         "transactions</b>, plus 3&ndash;4% annualised churn on $5K&ndash;$10K/mo offers. "
         "The proof is the operational metric a scammer cannot fake, not a testimonial."),
        ("&ldquo;What do the AI models say about you&rdquo; is one of his five systems",
         "He treats ChatGPT, Gemini, Claude and Google's AI overview as a funnel step. His "
         "example: a client whose real price was $17,000&ndash;$26,000 had an old podcast "
         "review quoting &ldquo;it might be 5K&rdquo; ranking in AI answers. Prospects "
         "arrived on calls anchored at $5K, saw $17K, and the close rate collapsed. "
         "We ran an AI visibility audit and scored 22/100 &mdash; he is treating that same "
         "score as a show-rate and close-rate input, not a branding vanity metric."),
        ("The didn't-show-up survey email, one line long",
         "Subject line: <i>feedback</i>. Body: <i>curious why you didn't show up tonight. "
         "Appreciate your feedback trying to improve.</i> The answers become next month's "
         "confirmation-page breakout videos. It is the cheapest feedback loop in the whole "
         "system and we do not run it."),
        ("No price on any page. No guarantee anywhere.",
         "The replay page writes out the entire MIM pitch &mdash; 7 weeks, video library, "
         "community, certification &mdash; and never names a number. Price appears only on "
         "the live call, and inside the class as $5,000. There is no risk reversal of any "
         "kind, on any asset. He substitutes the Stripe dispute rate for a guarantee."),
        ("Buy and Call, side by side, at the same moment",
         "The closing slide is two QR codes under the words <b>Buy</b> and <b>Call</b>. "
         "Self-serve checkout and book-a-call are offered simultaneously rather than "
         "sequentially, so a ready buyer never has to sit through a call to hand over "
         "$5,000."),
        ("He refuses payment plans out loud, as positioning",
         "<i>&ldquo;We don't have in any way, shape or form payment plans. It's either you "
         "got the money or you don't. We don't want to sell to people we have to chase.&rdquo;</i> "
         "Paired with the on-slide line <b>&ldquo;Expensive betrays you&rdquo;</b>, the "
         "no-plan policy is sold as a filter rather than apologised for."),
        ("Two businesses, one domain, and the cheap one is the content engine",
         "<code>/breakthroughsession</code> sells a $2,000 in-person session to founders "
         "doing $200K+/mo, filmed for YouTube. He says the plainly: <i>&ldquo;I am doing this "
         "at a very cost effective rate to get content for the channel, because these act "
         "as a great top of funnel viewership generation source.&rdquo;</i> The offer is "
         "priced to be filmed, not to be profitable."),
        ("The build is disposable on purpose",
         "bolt.new SPA, four Wistia videos, a Meta pixel and a Zapier catch hook. No "
         "ClickFunnels, no GHL, no CRM form. Total build is one page router and a webhook "
         "&mdash; which is why he could stand it up, run one 38-day flight, and abandon it "
         "without cost."),
    ],

    "FUNNEL": [
        ("Paid Meta ad &rarr; free class",
         "facebook.com/ads/library/?view_all_page_id=234697063572758",
         "Three video cuts of one script, Apr 5 &ndash; May 11 2026. Hook: "
         "&ldquo;Your Show Rates Are Down &mdash; Here's the Fix.&rdquo; Zero active today."),
        ("Registration", "jeremysworkshops.com/",
         "Countdown to April 8th, one testimonial, then first / last / email / phone plus an "
         "SMS consent box. Still live, countdown at zero."),
        ("Confirmation", "jeremysworkshops.com/confirmation",
         "8m58s video opening with a live Stripe screenshare, then two homework items: "
         "whitelist us, and go watch me on YouTube."),
        ("Pre-class nurture", "&mdash; not captured &mdash;",
         "&ldquo;Value dense&rdquo; emails targeting a 50%+ open rate, plus the Hammer Them "
         "SMS campaign. Described on-slide; never entered our inbox because we do not submit "
         "phone numbers."),
        ("The live class", "Zoom, 1h 26m",
         "Five backend selling systems taught, then the MIM pitch from roughly the 60-minute "
         "mark."),
        ("Replay page", "jeremysworkshops.com/replay",
         "Full replay plus the entire MIM pitch written out. No price. Both CTAs go straight "
         "to the calendar."),
        ("Book a call", "go.oncehub.com/MasterInternetMarkting",
         "OnceHub, 30 minutes. No application, no qualification, no price beforehand."),
        ("Buy or Call", "two QR codes on the closing slide",
         "Self-serve purchase and book-a-call offered at the same moment. $5,000, no payment "
         "plans, no guarantee."),
        ("Separate lane &mdash; $2,000 session", "jeremysworkshops.com/breakthroughsession",
         "Typeform gates on MRR ($200K/mo minimum), a human verifies by text, payment is taken, "
         "then a scheduler link is released."),
    ],

    "TRANSCRIPT_GROUPS": [
        ("The live class (1h 26m)", [os.path.join(PKG, "Transcript/transcript.md")]),
        ("Funnel videos", sorted(glob.glob(os.path.join(PKG, "Transcript/confirmation.md")) +
                                 glob.glob(os.path.join(PKG, "Transcript/vsl.md")) +
                                 glob.glob(os.path.join(PKG, "Transcript/breakthrough.md")))),
    ],

    "SLIDE_PAGES": [
        ("Slides", "slides.html", "Screenshots", "web_",
         "77 wide-shot frames from the April 8 class. This is a stage-filmed talk, not a "
         "screen share &mdash; the camera cuts constantly to close-ups where the slide text "
         "is a full-bleed background sliced by his head. Those 118 frames were pulled out; "
         "what is left is every frame where the whole slide is readable."),
    ],

    "DECKS": [
        ("The Backend Blueprint — April 8 2026", 77,
         "https://docs.google.com/presentation/d/1B_dMovpAx1sUF_suJEMHyrfYP7ZVFhVCdxi0UjFnGTs/edit"),
    ],

    "VIDEOS": [
        ("01_live_class_replay_apr8_1080p.mp4", 5168, "1.2 GB",
         "The live class replay. Wistia <code>32yqc9fvjq</code>, native 4K, pulled at 1080p."),
        ("02_confirmation_video_1440p.mp4", 538, "299 MB",
         "The confirmation-page video. The live Stripe screenshare. Wistia <code>c33ftuv39i</code>."),
        ("03_vsl_1440p.mp4", 327, "185 MB",
         "The 5m27s VSL. Wistia <code>halc1r9mwp</code>. Not currently wired to any live page."),
        ("04_breakthrough_session_1080p.mp4", 204, "38 MB",
         "The $2,000 in-person session pitch. Wistia <code>pqhpi82dia</code>."),
    ],

    "ANALYSIS": """
<div class="note"><b>The one thing worth stealing.</b> Urgency video first, information
videos second. He claims a single urgency video at the top of a confirmation page moved a
webinar show rate 19 points, and that 19 information videos added only 4 more. Our
confirmation page currently does neither &mdash; it confirms, and that is all it does.</div>

<h2 class="sec">The five backend selling systems, as he teaches them</h2>
<div class="tablewrap"><table>
<tr><th>#</th><th>System</th><th>What it actually is</th><th>His claim</th></tr>
<tr><td>1</td><td>Confirmation page best practices</td>
<td>One urgency video at the top, then up to 19 &ldquo;breakout&rdquo; videos answering the
objections the sales team is sick of hearing</td>
<td>+19 pts show rate from the urgency video alone; +4 from the 19 info videos</td></tr>
<tr><td>2</td><td>Value dense email sequences</td>
<td>Hand-written, value-first pre-class emails. He gives the whole sequence away as a Google
Doc to anyone who stays to the end of the class</td>
<td>Target open rate <b>50%+</b>, stated on slide</td></tr>
<tr><td>3</td><td>The Hammer Them campaign</td>
<td>SMS/DM saturation between opt-in and the event</td>
<td>Text has a higher connection rate than email; be valuable, not a reminder</td></tr>
<tr><td>4</td><td>Setter pre-call best practices</td>
<td>The setter is the first human impression, so grooming and framing are treated as
conversion levers</td>
<td><i>&ldquo;Your setters better look sharp and not look like shit&rdquo;</i></td></tr>
<tr><td>5</td><td>AI manipulation mastery</td>
<td>Auditing and shaping what ChatGPT / Gemini / Claude / Google AI Overview say about your
company and your price</td>
<td>A stale price in an AI answer nuked a client's close rate</td></tr>
</table></div>

<h2 class="sec">How the 86 minutes are actually built</h2>
<div class="tablewrap"><table>
<tr><th>Time</th><th>Beat</th><th>What he is doing</th></tr>
<tr><td>00:00</td><td>Frame</td><td>Names the outcome in the first sentence: show rates, then close rates, then cycle length</td></tr>
<tr><td>00:01</td><td>Exercise</td><td>&ldquo;Close your eyes&rdquo; &mdash; puts the audience inside the scroll to make the next stat land</td></tr>
<tr><td>00:02</td><td>Stat</td><td>Gen Z gives 6.5 seconds of focused attention per post, and it gets worse with age</td></tr>
<tr><td>00:03</td><td>Named concept</td><td><b>Scanner mode &rarr; justification mode.</b> The whole class hangs off this one distinction</td></tr>
<tr><td>00:04</td><td>Analogy</td><td>The Komodo Miami restaurant: reviews, lowest ratings, photos, asking a friend</td></tr>
<tr><td>00:07</td><td>Enumerate</td><td>The five places a lead judges you after opting in</td></tr>
<tr><td>00:08</td><td>Solution map</td><td>One system per judgement point, each with a 13&ndash;32 page SOP behind it</td></tr>
<tr><td>00:09&ndash;01:00</td><td>Teach</td><td>The five systems, with a client case behind each</td></tr>
<tr><td>01:00</td><td>Transition</td><td>&ldquo;Drop a 1 in the chat if I can make an offer to you tonight&rdquo;</td></tr>
<tr><td>01:02</td><td>Offer</td><td>7 weeks, week by week, then lifetime access, then Jeremy AI</td></tr>
<tr><td>01:08</td><td>Price framing</td><td>&ldquo;Expensive betrays you&rdquo;, no payment plans, $5,000</td></tr>
<tr><td>01:12</td><td>Downsell</td><td>Jeremy AI at $300/mo or $2,000/yr for anyone not taking MIM</td></tr>
<tr><td>01:15+</td><td>Close</td><td>Buy QR and Call QR side by side, then testimonial screenshots on loop</td></tr>
</table></div>

<h2 class="sec">Proof, and what kind it is</h2>
<div class="grid g2">
<div class="card"><h3>Operational, not aspirational</h3><p>0.37% lifetime Stripe dispute rate
over 7,241 transactions. 3&ndash;4% annualised churn. These are numbers that only exist if the
business is real, and they are shown live on screen rather than as a graphic.</p></div>
<div class="card"><h3>Chat screenshots, not video testimonials</h3><p>Almost all social proof
is screenshots of the private community and DMs &mdash; &ldquo;$5000 for this level of
information is just insane&rdquo;, &ldquo;bought your 5k offer Friday&rdquo;, a member
reporting $3,300 of ad spend returning $48,044. Text screenshots read as unstaged in a way a
filmed testimonial does not.</p></div>
<div class="card"><h3>The price is inside the proof</h3><p>He never puts a price slide up. The
number arrives through other people's mouths in screenshots. By the time he says $5,000 out
loud, three testimonials have already said it for him.</p></div>
<div class="card"><h3>No guarantee at all</h3><p>Not a conditional one, not a 30-day one.
Nothing. The dispute rate is doing the job a guarantee normally does.</p></div>
</div>

<h2 class="sec">Worth taking</h2>
<div class="grid g2">
<div class="card"><h3>Put an urgency video on the confirmation page</h3><p>Not a reminder
video. A real reason this specific class matters this specific week. He claims 19 points of
show rate off one video and the ordering rule is explicit: urgency first, information
second.</p></div>
<div class="card"><h3>Ship the didn't-show survey email</h3><p>Subject &ldquo;feedback&rdquo;,
one line, sent to every no-show. It costs nothing and it is the only way to get the real
reason rather than the guessed one. Feed the answers straight into the confirmation-page
videos.</p></div>
<div class="card"><h3>Mine sales-call transcripts for breakout video topics</h3><p>He tells the
room to dump every transcript into Claude Projects and pull the recurring objections out, then
film one short video per objection and stack them under the urgency video.</p></div>
<div class="card"><h3>Show an operational number as proof</h3><p>His dispute rate is the
single most credible thing in the funnel and it costs nothing to show. We have equivalents.
The instinct to lead with student wins is not wrong, but it is the same thing every
competitor does.</p></div>
<div class="card"><h3>Offer Buy and Call at the same time</h3><p>Two QR codes, one slide. A
prospect who is already sold should never be forced through a call to pay.</p></div>
<div class="card"><h3>Treat AI answers as a funnel step</h3><p>Our own AI visibility audit came
back 22/100. He frames that as a show-rate and close-rate leak, not a branding problem, and
built one of five systems around it.</p></div>
</div>

<h2 class="sec">What we could not observe</h2>
<p>The opt-in was never submitted &mdash; the form requires a phone number, and we do not
fabricate one, so the email sequence and the Hammer Them SMS campaign are described by him
on-slide but not captured in our own inbox. The $5,000 price is verified from on-slide
testimonial screenshots and from the spoken transcript, not from a price slide or a checkout
page; there is no checkout URL exposed anywhere in the bundle, only the two QR codes on the
closing slide. Conversion numbers, registration volume and actual spend are all unknown &mdash;
the only hard traffic fact is a 38-day Meta flight across three creatives.</p>
""",
}

build(CONFIG)
