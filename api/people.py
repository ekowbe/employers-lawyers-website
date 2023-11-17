"""module to store info for all peeps"""

dave_descrip = '''
David is a dedicated labor and employment law attorney for 
employers. He battles for employers facing workplace law issues. 
He is regarded as a skilled trial attorney that tries employment 
discrimination, wage and hour, whistleblowing, and termination 
cases to juries, judges, and arbitrators in New York and Connecticut. 
He also assists employers in investigations concerning harassment, 
sexual harassment, theft, unfit for work issues and reductions in force. 
Dave strives to develop legal strategies that are aligned to employer 
objectives and goals.
<br><br>
Dave has focused his practice on labor and employment law and education 
law for many years. Since 1999 he has maintained law offices in both New 
Haven and New London. He has been named as a Connecticut and New England 
Super Lawyer in his field since 2007. He is also recognized yearly for 
excellence by Best Lawyers and Best Law Firms (Best Lawyers is a partner 
with US News and World Report). Like Bill, David was an athlete in college. 
At Yale he played baseball and received the Gerald R. Ford Scholar Athlete 
Award. After Yale, he attended Hofstra Law where he was recognized for his 
achievements in labor law with scholarships and awards. He was captain of 
the school’s national labor law moot court team and received the Labor Law Award 
at graduation.
<br><br>
David frequently presents and provides training on human resource topics, 
corporate governance, union avoidance, effective discipline, fitness for 
duty, and sexual harassment. He has served as an adjunct professor at 
Post University. He has served on not-for-profit Boards including the 
Connecticut Society to Prevent Blindness and Easter Seals Goodwill. He 
was a founding member of Amity Pop Warner Football and Cheerleading, Inc. 
and was a Bethwood Baseball Board member in Woodbridge, CT.
'''

bill_descrip = """
Bill has focused on labor and employment law issues from an 
employer’s perspective since law school where he earned the 
school's Labor Law Award.
<br><br>
For just under 30 years, Bill has assisted employers in 
successfully resolving complex labor and employment issues. 
His practice spans all of labor and employment law, including, 
but not limited to counseling employers on the entire spectrum 
of labor and employment issues, successfully litigating 
employment cases involving age, race, sex, national origin, 
constructive discharge, defamation, state and federal labor laws, 
FMLA, wage and hour, and retaliation cases.
<br><br>
In addition to employment counseling, litigating and arbitrating 
labor and employment cases, Bill negotiates collective bargaining 
agreements, drafts and negotiates employment contracts, drafts 
severance agreements, drafts employee handbooks, and drafts other 
employer policies and procedures.
<br><br>
Bill also presents seminars and conducts supervisory training on 
issues including, but not limited to, sexual harassment and other 
forms of workplace harassment, ADA and FMLA, internal investigations, 
workplace violence and workplace privacy.
<br><br>
Additionally, Bill was a contributing author of a published treatise 
on Connecticut labor and employment law. He has also served as an 
instructor for certificate programs in human resources management 
and personnel relations and the law at Teikyo Post University.
<br><br>
Bill has been consistently recognized as one of “Connecticut’s 
Super Lawyers” and ”New England’s Super Lawyers” by Law and 
Politics as well as "Best Lawyers."
"""

ian_descrip = """
Ian, who was a partner at a large Connecticut based law firm 
for eleven years after practicing law in New York, focuses his 
practice on complex civil litigation and risk management 
counseling, representing businesses in a broad range of cases, 
including unfair business practices, trade secret disputes, 
officer and director liability, securities litigation, 
purchase price adjustment disputes, professional malpractice, 
business torts, class actions and contract and real estate 
disputes.
<br><br>
Ian has experience in all aspects of case management, including 
first chair of trials in federal and state court and in complex 
arbitrations. He has significant experience working with firm 
clients in an advisory role to develop risk management strategies 
for litigation avoidance, assess liability exposure and settlement 
negotiations. Ian's practice also includes management of litigation 
dockets and general business counsel duties for public and private 
organizations.
"""

tracy_descrip = """
Tracy Yentsch Inzero is a Paralegal and Office Manager at Ryan & Ryan.
She provides invaluable assistance in workplace investigations for the 
Ryan & Ryan firm. She has been employed by Ryan & Ryan since 2015.  
She assists with research and maintains large litigation files. 
She also assists with pleadings and correspondence. She has been employed 
in the field for over twenty years.
"""

people = {
    "Dave": {
        'name': 'David A. Ryan',
        'img_src': "/static/img/people/Dave.png",
        'title': 'Attorney',
        'tel': '+1 203 752 9794',
        'email': 'david.ryan@ryan-ryan.net',
        'descrip': dave_descrip,
        'experience': ["Employment Litigation", "Labor Law", "Education Law", "Municipal Law"],
        'education': ["B.A., Yale University", "J.D., Hofstra University School of Law"],
        'admissions': {
            'bars': ['Connecticut', 'New York'],
            'courts': ['United States District Court', 'Court of Appeals for the Second Circuit']
        },
        'affiliations': ["Connecticut Bar Association, Labor and Employment Law Section",
                         "American Bar Association"],
        'awards': ['Connecticut Super Lawyers, 2007-2023',
                   'New England Super Lawyers, 2007-2023',
                   'Best Lawyers (US News and World Report)',
                   'AV Rated, 2023'
                   ],
        'boards': ['Easter Seals Goodwill',
                   'Connecticut Society to Prevent Blindness',
                   'Amity Pop Warner Football and Cheerleading, Inc.',
                   'Bethwood Baseball in Woodbridge, CT'
                   ]
    },

    "Bill": {
        'name': 'William A. Ryan',
        'img_src':"/static/img/people/Bill.png",
        'title': 'Attorney',
        'tel': '+1 203 752 9794',
        'email': 'william.ryan@ryan-ryan.net',
        'descrip': bill_descrip,
        'experience': ["Employment Litigation", "Labor Law", "Education Law", "Municipal Law"],
        'education': ["B.A., Williams College", "J.D., Hofstra University School of Law"],
        'admissions': {
            'bars': ['Connecticut'],
            'courts': ['United States District Court']
        },
        'affiliations': ["Connecticut Bar Association, Labor and Employment Law Section",
                         "American Bar Association"],
        'awards': ['Connecticut Super Lawyers, 2007-2023',
                   'New England Super Lawyers, 2007-2023',
                   "America's Best Attorney"
                   ]
    },

    "Ian": {
        'name': 'Ian E. Bjorkman',
        'img_src': "/static/img/people/Ian.png",
        'title': 'Attorney',
        'tel': '+1 203 752 9794',
        'email': 'ian.bjorkman@ryan-ryan.net',
        'descrip': ian_descrip,
        'experience': ["Corporate Counsel", "Litigation", "Complex and Multi-District Litigation", "Trade Secrets", "Unfair Competition", "Torts", "Civil Practice"],
        'education': ["B.A., New York University", "J.D., Brooklyn Law School"],
        'admissions': {
            'bars': ['Connecticut', 'New York'],
            'courts': ['United States District Court',
                       'Court of Appeals for the Second Circuit'
                      ]
        }
    },

    "Tracy": {
        'name': 'Tracy Yentsch Inzero',
        'img_src': "/static/img/people/Tracy.png",
        'title': 'Attorney',
        'tel': '+1 203 752 9794',
        'email': 'tracy.yentsch@ryan-ryan.net',
        'descrip': tracy_descrip,
        'education': ["B.A., Eastern Connecticut State University", "Paralegal Certificate from Boston University"]
    }
}