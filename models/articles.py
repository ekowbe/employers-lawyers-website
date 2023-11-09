"""module for all articles"""


def dict_to_text(text_dict):
    """converts article dict to str"""
    text = ""
    for val in text_dict.values():

        if val['type'] == 'heading':
            t = f"<h3 class='fw-light pt-5 mb-2 text-dark'>{val['text']}</h3>"

        if val['type'] == 'subheading':
            t = f"<h4 class='fw-light pt-5 mb-2 text-dark'>{val['text']}</h4>"

        if val['type'] == 'par':
            t = f"""
                    <p class="lead text-justify">
                    {val['text']}
                    </p>
                """

        if val['type'] == 'list':
            t = "<ul>"

            for el in val['text']:
                t += f"<li class='lead'>{el}</li>"

            t += "</ul>"
    
        text += t
    return text

connecticut_paid_leave = """
Beginning January 1, 2021, all private sector employers in Connecticut (with the exception 
of certain private school employees) are required to make a payroll deduction of .5% from 
their employees’ pay to fund the State’s new Paid Family and
Medical Leave program. Public sector employers are not included in the requirement to make
the payroll deductions and will not be required to grant leave under the program unless and
until a bargaining unit negotiates inclusion into the program. Similar to the State’s
unemployment program, the payments deducted from employees’ paychecks are submitted on a
quarterly basis and deposited into a trust fund, which will be used to fund the program.

Employees cannot begin taking leave under the program until January 2022. In general, the law
provides for 12 weeks of paid leave during any 12-month period, with additional leave time
permitted due to pregnancy. The reasons for leave are significantly expanded from those
currently permitted under the State’s current Family and Medical Leave Act. These
reasons include leave to care for individuals who have a close association with the employee that
the employee shows to be the equivalent of a family member. We will provide you with
additional information on the leave benefits that will be available to employees as we get
closer to the date when employees can apply for leave under the program.
"""

connecticut_paid_leave_article = {
    'title': 'Grassroots Union Activity',
    'author': 'David Ryan',
    'date': 'February 10, 2021',
    'text': connecticut_paid_leave
}




grassroots_article_text = """
<h3 class="fw-light pt-5 mb-2 text-dark">Union Activity - More to Report</h3>

<p class="lead text-justify">
In our last issue we discussed the unanticipated rise in unionization efforts occurring
nationwide—that is derived at least in part from COVID-19. The pandemic’s upheaval of the
traditional working environment and increased unemployment rates has spawned
anti-management thinking amongst employees at several high-profile workplaces. Increased
digital connectivity is also linked to the new flurry of activity.
</p>

<h3 class="fw-light pt-5 mb-2 text-dark">Grassroots Movement</h3>

<p class="lead text-justify">
This uptick in unionization is described by union attorneys we know as a grassroots movement
of employees who are 30 years old or younger. We are told that most of these actions are not
sponsored or organized by the AFL-CIO; rather, they are initiated at the local workplaces
themselves. For instance, over 250 Starbucks shops have filed petitions for elections with the
NLRB, and 54 of those have had successful results. Similarly, fiber contractors in Kansas City
successfully voted to unionize their small office in March becoming the first workers with
collective bargaining rights within the new one year-old Alphabet Workers Union. Workers at an
Amazon warehouse in New York City recently voted to form the first union at the second-largest
U.S. private employer and joined the Amazon Labor Union. Similar spikes in union activity
have occurred at Apple, Chipotle, and Trader Joe’s.
</p>

<h3 class="fw-light pt-5 mb-2 text-dark">Pro-Union Politics</h3>
<p class="lead text-justify">
Unionization is believed to be easier today due to pro-union politics. President Biden, vowing to
be the “most pro-union president ever,” has filled the NLRB with people beholden to the
interests of organized labor in an effort to deTrumpify the NLRB. As discussed in our last Eye,
Biden has also taken aim at captive audience mandatory meetings. Earlier this year, the
president met with 39 national labor lead text-justifyers, including Christian Smalls, the head of the
Amazon Labor Union, sending a powerful pro-union message to employers. It should not be
surprising that Unions have won more elections in 2022 than they have in nearly 20
years.
</p>

<h3 class="fw-light pt-5 mb-2 text-dark">What Should Employers Do?</h3>
<p class="lead text-justify">
Based on the current popularity of Unions, pro-union politics and the momentum caused by
recent successes in union activity, employers should brace themselves and assess how they
would handle a union campaign/election. In particular, employers should expect a return to
Obama-era NLRB rules which represented an attempt to restore the rights of organized labor. For
example, at the beginning of last month the NLRB proposed a rule that expands the meaning of
joint-employer which would make more staffing companies and their clients vulnerable to
elections and representation.
</p>

<p class="lead text-justify">
Employers relying on employees provided through third party vendors should carefully examine
their service contracts, focusing on the language reserving the right to directly or indirectly
control terms and conditions of employment. We are well-equipped to help you navigate through
these and other legal and strategic considerations governing the union representation process,
unfair labor practices, and collective bargaining.
</p>

<h3 class="fw-light pt-5 mb-2 text-dark">More Pro Employee Laws from our Neighbors</h3>
<p class="lead text-justify">
In New York City, The Wrongful Discharge Law makes it much more difficult for
fast-food restaurant chains with 30+ locations to terminate workers. The law, established in
January 2021, prevents covered employers from firing workers without “just cause,” which is
language often found in union contracts. The Restaurant Law Center, a legal affiliate of the
National Restaurant Association, challenged this law earlier in the year, but its case in U.S.
Federal District Court was dismissed. The case is now on appeal at the Second Circuit awaiting
oral argument since briefs have been filed. We’ll keep you posted on the Second Circuit’s ruling,
which will likely address Federal pre-emption as well as Commerce Clause issues.
</p>
"""

grassroots_article = {
    'title': 'Grassroots Union Activity',
    'author': 'David Ryan',
    'date': 'February 10, 2021',
    'text': grassroots_article_text
}

attracting_talent_text = """
<h3 class="fw-light pt-5 mb-2 text-dark">Thoughts on Attracting and Keeping Talented Workers</h3>

<p class="lead text-justify">
In our last two issues of Eye on the Law we discussed labor shortages in Connecticut and New
England (excluding NYC and Boston). Several other factors are noteworthy:
<ol>
<li> The birth rate is declining; </li>
<li> The rate of employee turnover is reported to be 25%; and </li>
<li> Approximately 40% of the work force is at least passively looking for other jobs. </li>
</ol>
</p>

<p class="lead text-justify">
SHRM, the Society for Human Resource Management has published numerous articles on the
labor shortage and what is trending in terms of employee desires and demands.
</p>

<p class="lead text-justify">
Given these issues and our labor shortage, what should employers focus on in attracting and
keeping talent? Below are some thoughts and links to more information. We will continue to
discuss these and other ideas in the future since many experts, including SHRM’s talented CEO
Johnny C. Taylor, Jr., are reporting that human capital has become the primary issue for US
companies. Three important and immediate considerations are:
</p>


<h4 class="fw-light pt-5 mb-2 text-dark">Higher Pay</h4>
<p class="lead text-justify">
It is clear at this time that the number one factor to attract talented
employees is more pay. They are less interested in benefits such as paid time off, which
was reported to be important two years ago. Talented employees hear their friends talking
about larger salaries, signing bonuses and year-end bonuses. They realize that this is a
unique labor market that presents unique opportunities.
</p>


<h4 class="fw-light pt-5 mb-2 text-dark">Consider co-opting or co-sourcing employees</h4>
<p class="lead text-justify">
Many of our clients are already using this method to fill or partially fill positions that require special licensing and degrees.
Because of inflation and the potential for individual development, many workers are
willing to consider part–time hybrid work models. We have seen some clients enjoy
success with co-opting employees, particularly in the public sector. For more information,
click on this co-sourcing link.
</p>

<h4 class="fw-light pt-5 mb-2 text-dark">Quality training and development with top managers</h4>
<p class="lead text-justify">
Talented employees are becoming more desirous of real training and real access to company lead text-justifyers. They want
the opportunity to learn from the best that you have and can offer in the area of
management training. They want to hear the war stories and learn from them. For more,
click this link from SHRM about additional opportunities employees want.
</p>

<h3 class="fw-light pt-5 mb-2 text-dark">Important Legislation - State and Federal</h3>

<h4 class="fw-light pt-5 mb-2 text-dark">March 3, 2022 Biden signs new law amending the Federal Arbitration Act (“FAA”) </h4>
<p class="lead text-justify">
The legislation bans compelled arbitration of sexual harassment and sexual assault
cases in employment. The new law has some retroactive effect - it bans the
enforcement of prior employment arbitration agreements that forced employees
into arbitration on these issues. While the amendment does not affect other
discrimination claims, the Biden administration has made it clear that it intends to
end forced arbitration for all employees regarding all types of employment
discrimination claims. The Amendment gives employees the option to invalidate
arbitration agreements and class action waivers on the issues of sexual
assault and sexual harassment claims.
</p>

<h4 class="fw-light pt-5 mb-2 text-dark">State of Washington passes legislation banning non-disclosure clauses and
agreements</h4>

<p class="lead text-justify">
Effective June 9, 2022, it shall be unlawful for Washington employers to require
or even ask employees to sign workplace confidentiality agreements. In addition,
the legislation bans non-disclosure agreements in settlement agreements and even
certain types of non-disparagement provisions if they restrict an individual’s right
to discuss discrimination, wage issues and other employment issues, including
alleged violation(s) of public policy.
</p>

<p class="lead text-justify">
In a remote work or even hybrid form of reporting to work world this law effects
many employers throughout the US. Multi-state employers are again forced to
decide on whether they will choose uniformity in their policies or simply take
advantage of whatever laws help them on a state-to-state basis.
</p>

<p class="lead text-justify">
The number of states with legislated limitations for non-disclosure agreements
now stands at 12. They are:
</p>
<ul>
<li>California</li>
<li>Washington</li>
<li>Illinois</li>
<li>New Jersey</li>
<li>Oregon</li>
<li>Hawaii</li>
<li>Louisiana</li>
<li>New Mexico</li>
<li>Nevada</li>
<li>Tennessee</li>
<li>Maryland</li>
<li>Vermont </li>
<li>(Maine is considering legislation at this time);</li>
</ul>
<p class="lead text-justify">
Surprisingly, New York still allows for non-disclosure clauses in
pre-employment agreements and certain severance agreements.
</p>

<h3 class="fw-light pt-5 mb-2 text-dark">Amazon Facility in Staten Island Loses Union Election</h3>

<h4 class="fw-light pt-5 mb-2 text-dark">Independent Union JFK8 slays giant Amazon using new age messaging and old
school campaigning methods.</h4>

<p class="lead text-justify">
JFK8, an independent non-AFL-CIO affiliated Union, recently won a Union
election at an Amazon facility in New York. JFK8 organizers were successful in
large part due to the following:
</p>

<ul>
<li>A nationwide NLRB settlement in December 2021 with Amazon
eliminated an Amazon work rule which forced all employees to leave
Amazon facilities at the end of their shift.</li>
<li>This NLRB settlement allowed employees who were JFK8 lead text-justifyers and
supporters to engage in more face-to-face campaigning with co-workers in
break rooms and parking lots.</li>
<li>JFK8 lead text-justifyers also used the NLRB information disclosure rules to gain
access to voters at their residences in order to campaign using door-todoor approaches. In some cases, they waited to speak to co-workers at bus
stops.</li>
</ul>

<p class="lead text-justify">
Messaging included actual work issues as well as themes of inequality, racial
issues and global warming. JFK8 is aiming high - essentially broadcasting that all
Amazon workers should be organized. Post-election (NLRB) they have also
mentioned Apple and Google. We’re sure that a union handout or two must have had pictures of Amazon’s
Bezos vacationing on his super-sized yacht.
</p>
"""

attracting_talent_article = {
    'title': 'Attracting Talent and Keeping It',
    'author': 'David Ryan',
    'date': 'March 15, 2021',
    'text': attracting_talent_text
}

scotus_article_text_dict = {
    1: {
        'type': 'heading',
        'text': 'The Arbitration Landscape is Changing'
    },

    2: {
        'type': 'par',
        'text': """Recent decisions suggest that the US Supreme Court may be moving away from a
                    generalized pro-arbitration stance based on long established policy dating as far
                    back to the Steelworkers Trilogy in 1960. Instead, the Supreme Court seems to be
                    reaching decisions based on strict textual interpretation of the Federal Arbitration
                    Act (FAA)."""
    },

    3: {
        'type': 'par',
        'text': """ For example, Badgerow v. Walters resolves a key question about awarding
                    arbitrations in federal courts by applying FAA Sections 9 and 10 - 'a court may
                    look only to the application actually submitted to it in assessing its jurisdiction.'"""
    },
    4: {
        'type': 'par',
        'text': """Clients with arbitration agreements or those considering them should examine
                    arguments relating to strict analyses of the FAA rather than relying on generalized,
                    long established Supreme Court deference to arbitration as a matter of public
                    policy.'"""
    },
    5: {
        'type': 'heading',
        'text': "Why Workers Unionize"
    },
    6: {
        'type': 'par',
        'text': """In our last issue of Eye on the Law we discussed strategies employers can use to attract and
                    keep talented employees. In addition to a means of insuring a productive, skilled workforce
                    these tactics are important because, dissatisfaction with treatment by management remains
                    the primary reason that pushes workers to unionize. Starbucks, Amazon and Apple, three
                    giants previously thought to be untouchable in terms of employee collective action, have
                    experienced heightened union activity in recent months. Three important considerations are:"""
    },
    7: {
        'type': 'list',
        'text': ["The #MeToo movement", "The #BlackLivesMatter movement", "The Fight for $15 movement"]
    },
    8: {
        'type': 'par',
        'text': """These movements, propelled by the collective indignation of their proponents, facilitate a
                    culture of protest, which lends itself well to unionization. Other conditions, such as
                    perceived disparate pay (many articles about CEO compensation packages), perceived
                    unfair policies, and low levels of employee trust can cause employees to look to unions for
                    help or create their own union."""
    },
    9: {
        'type': 'par',
        'text': """Chris Smalls, the lead text-justifyer of the Amazon Labor Union, described Amazon’s long working
                    hours, short breaks, and discriminatory and haphazard hire-and-fire practices in in an
                    interview on the Daily Show. Ultimately, the pushes for union representation at behemoths
                    like Starbucks, Amazon and Apple may provide impetus for workers at smaller workplaces
                    to do the same."""
    },
    10: {
        'type': 'heading',
        'text': "Important Legislation and Court Actions"
    },
    11: {
        'type': 'subheading',
        'text': "May 17, 2022 Governor Lamont signs new law about “Captive Audience” meetings"
    },
    12: {
        'type': 'par',
        'text': """Effective July 1, 2022, it shall be unlawful for all employers to discipline or
                    terminate, or threaten to discipline or terminate, an employee for refusing to
                    attend employer-sponsored meetings, listen to a speech or view
                    communications primarily intended to convey the employer’s opinion about
                    religious or political matters, including decisions to join/not to join a labor
                    organization. While we think the statute, as it relates to labor organizations, is likely to be
                    challenged on federal preemption grounds, it is an indicator of union political
                    power."""
    },
    13: {
        'type': 'subheading',
        'text': """June 24, 2922 Roe v. Wade overturned"""
    },
    14: {
        'type': 'par',
        'text': """The US Supreme Court overturned the constitutional abortion right
                    established roughly 50 years ago in Roe v. Wade. This paves the way 
                    for many states to rollback abortion rights. According to
                    the Guttmacher Institute, 26 states may move to ban/limit abortion."""
    }

}

scotus_article_text = dict_to_text(scotus_article_text_dict)

scotus_article = {
    'title': 'SCOTUS Decisions and Unions',
    'author': 'David Ryan',
    'date': 'September 20, 2022',
    'text': scotus_article_text
}

reads = {
    grassroots_article['title']: grassroots_article,
    attracting_talent_article['title']: attracting_talent_article,
    scotus_article['title']: scotus_article,
}
