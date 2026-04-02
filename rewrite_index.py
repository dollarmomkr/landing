# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace Title
content = re.sub(
    r'<title>.*?</title>',
    '<title>DollarMom | 엄마의 눈으로 지키는 달러 자산 보험 메신저</title>',
    content
)

# Replace the color palette in style block (Lines ~20 to ~30)
palette_replacement = """            --bg-primary: #0a0a0f;
            --bg-secondary: #0a0a0f;
            --bg-card: #16161f;
            --bg-elevated: #16161f;
            --gold: #c9a84c;
            --gold-light: #e4c76b;
            --gold-dim: rgba(201, 168, 76, 0.15);
            --text-primary: #f0ece2;
            --text-secondary: #9a968e;
            --text-muted: #5a5750;
            --accent-blue: #2e8b57; /* Dollar Green */
            --accent-rose: #e88b56; /* Soft Orange Warning */
            --accent-emerald: #f5ede1; /* Soft Beige */
            --border: rgba(201, 168, 76, 0.12);"""
content = re.sub(r'--bg-primary: #0a0a0f;.*?--border: rgba\(201, 168, 76, 0\.12\);', palette_replacement, content, flags=re.DOTALL)

# Header Replace
header_replacement = """    <header class="site-header" id="siteHeader">
        <div class="header-inner">
            <a href="#" class="logo" onclick="showMainPage(); return false;">
                <div class="logo-icon" style="border-radius:50%; font-size:24px; font-weight:bold; background:linear-gradient(135deg, #c9a84c, #e4c76b); padding-right:2px; padding-bottom:1px; transform:none;">D<span style="font-size:12px; margin-left:1px; display:inline-block; transform:translateY(-5px);">♥</span></div>
                <div class="logo-text">DOLLAR<span style="font-family: 'Noto Sans KR', sans-serif; font-size:1.4rem; padding-left:2px;">MOM</span></div>
            </a>
            <nav class="header-nav">
                <a href="#briefing">달러 브리핑</a>
                <a href="#product101">달러 상품 101</a>
                <a href="#casestudy">케이스 스터디</a>
                <a href="#life">달러맘 라이프</a>
                <a href="#webinar">웨비나/이벤트</a>
                <a href="#" class="header-cta" onclick="showApplicationForm()">15분 상담 예약</a>
                <button type="button" id="headerLoginBtn" class="header-login-btn" onclick="toggleHeaderLogin()">로그인</button>
            </nav>
            <button class="mobile-toggle" onclick="document.querySelector('.header-nav').classList.toggle('mobile-open')">☰</button>
        </div>
    </header>"""
# Find boundaries of the header
import re
header_pattern = r'<header class="site-header".*?</header>'
content = re.sub(header_pattern, header_replacement, content, flags=re.DOTALL)

# Hero Content Replace
hero_content_replacement = """        <div class="hero-content">
            <div class="hero-eyebrow" style="letter-spacing:0.1em; color:var(--text-secondary);">엄마의 눈으로 지키는 달러 자산 보험 메신저</div>
            <h1 class="hero-title">
                어려운 금융 말고,<br><span class="gold">내게 맞는 달러 전략</span>
            </h1>
            <p class="hero-subtitle">
                환율·노후·자녀 교육비가 걱정되시나요?<br>
                달러맘이 쉽고 명확하게 당신의 상황에 꼭 맞는 답을 찾아드립니다.
            </p>
            <p class="hero-date" style="font-family:var(--font-body); letter-spacing:0.02em; color:var(--text-primary); margin-bottom: 30px;">따뜻함과 전문성으로 든든한 미래를 준비하세요.</p>
            <div class="hero-actions">
                <button class="btn-gold" style="background: linear-gradient(135deg, var(--gold), var(--accent-blue)); color:white;" onclick="showApplicationForm()">15분 상담 예약</button>
                <button class="btn-outline" onclick="window.open('http://pf.kakao.com/', '_blank')">카카오로 상담</button>
            </div>
        </div>"""
content = re.sub(r'<div class="hero-content">.*?</div>\s*<!-- Scroll Indicator -->', hero_content_replacement + '\n\n        <!-- Scroll Indicator -->', content, flags=re.DOTALL)

# Replace the body sections (Courses to CTA)
sections_replacement = """    <!-- ═══════ DOLLAR BRIEFING ═══════ -->
    <div class="divider"></div>
    <section class="section" id="briefing">
        <div class="section-label">Dollar Briefing</div>
        <h2 class="section-title">오늘의 달러 브리핑</h2>
        <p class="section-desc">핵심만 짚어주는 환율과 글로벌 경제 뉴스</p>
        <div class="courses-grid">
            <div class="course-card">
                <span class="course-badge badge-partner" style="background:#2e8b5722; color:#2e8b57; border-color:#2e8b5755;">News</span>
                <h3 class="course-name">미 연준 금리 인하, 달러 예금 어떡하죠?</h3>
                <p class="course-sub">금리 인하 시기, 안정성을 지키면서 수익을 방어하는 달러 예금 활용법 가이드.</p>
                <div class="tags" style="margin-bottom:1.5rem;"><span class="tag">금리 인하</span><span class="tag">달러 예금</span></div>
                <button class="course-btn">자세히 보기</button>
            </div>
            <div class="course-card featured" style="border-color:var(--gold);">
                <span class="course-badge badge-partner" style="background:var(--gold-dim); color:var(--gold); border-color:var(--gold);">Market</span>
                <h3 class="course-name">원달러 환율 1,400원 돌파, 환전할까?</h3>
                <p class="course-sub">고환율 시대에 똑똑하게 달러 자산을 나누어 매입하는 분할 매수 팁과 시기.</p>
                <div class="tags" style="margin-bottom:1.5rem;"><span class="tag">고환율</span><span class="tag">분할 매수</span></div>
                <button class="course-btn">자세히 보기</button>
            </div>
            <div class="course-card">
                <span class="course-badge badge-partner" style="background:#f5ede122; color:#f5ede1; border-color:#f5ede155;">Report</span>
                <h3 class="course-name">금융 변동성과 달러의 매력</h3>
                <p class="course-sub">불확실한 경제 상황 속에서 달러가 가지는 안전 자산으로서의 가치.</p>
                <div class="tags" style="margin-bottom:1.5rem;"><span class="tag">안전 자산</span><span class="tag">시장 변동성</span></div>
                <button class="course-btn">자세히 보기</button>
            </div>
        </div>
    </section>

    <!-- ═══════ DOLLAR PRODUCT 101 ═══════ -->
    <div class="divider"></div>
    <section class="section" id="product101">
        <div class="section-label">Dollar Product 101</div>
        <h2 class="section-title">달러 상품 101</h2>
        <p class="section-desc">알고 나면 쉬운 달러 예금, 달러 보험의 기본 개념과 차이점</p>
        <div class="features-grid">
            <div class="feature-card">
                <span class="feature-icon">🏦</span>
                <h3 class="feature-title">달러 예금 기초</h3>
                <p class="feature-desc">언제든 넣고 뺄 수 있는 현금성 자산. 금리 변동에 따른 이자 수익과 환차익까지 기대할 수 있는 기본 상품입니다.</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">🛡️</span>
                <h3 class="feature-title">달러 종신 보험</h3>
                <p class="feature-desc">가족을 위한 든든한 안전망. 변동성이 적고 장기적으로 목돈 마련 및 보장의 두 마리 토끼를 잡을 수 있습니다.</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">📈</span>
                <h3 class="feature-title">달러 연금</h3>
                <p class="feature-desc">안정적인 노후 현금 흐름 창출. 환율 상승 시 연금 수령액이 늘어나는 구조로 노후 자산 방어에 유리합니다.</p>
            </div>
        </div>
    </section>

    <!-- ═══════ CASE STUDY ═══════ -->
    <div class="divider"></div>
    <section class="section" id="casestudy">
        <div class="section-label">Case Study</div>
        <h2 class="section-title">달러맘 실전 사례 (케이스 스터디)</h2>
        <p class="section-desc">나와 비슷한 고민을 했던 엄마들, 소상공인들의 실전 사례 모음</p>
        
        <div class="solutions-overview-grid">
            <div class="solution-overview-card">
                <span class="sol-icon">👩‍👧</span>
                <h3 class="sol-title">40대 맞벌이 (자녀 교육비)</h3>
                <p class="sol-desc">아이 유학 자금을 대비해 시작한 달러 예금·연금 분산 플랜 실전 코칭 후기.</p>
            </div>
            <div class="solution-overview-card">
                <span class="sol-icon">☕</span>
                <h3 class="sol-title">50대 카페 사장 (노후 준비)</h3>
                <p class="sol-desc">고정 매출에서 일부를 달러 종신으로 돌려 안정적인 은퇴 자금을 마련한 이야기.</p>
            </div>
            <div class="solution-overview-card">
                <span class="sol-icon">🏢</span>
                <h3 class="sol-title">30대 프리랜서 (자산 증식)</h3>
                <p class="sol-desc">환차익과 복리를 동시에 노리는 달러 적립식 투자 첫걸음 성공 사례.</p>
            </div>
        </div>
    </section>

    <!-- ═══════ LIFE & WEBINAR ═══════ -->
    <div class="divider"></div>
    <section class="section" id="life" style="padding-bottom:20px;">
        <div class="section-label">DollarMom Life & Event</div>
        <h2 class="section-title">달러맘 라이프 / 웨비나</h2>
        <p class="section-desc">일상 속 경제 이야기부터 실시간으로 소통하는 온라인 라이브까지</p>
        
        <div class="courses-grid" style="grid-template-columns: repeat(2, 1fr);">
            <div class="course-card" id="life-card" style="background:var(--bg-secondary);">
                <span class="course-badge badge-partner" style="background:rgba(232, 139, 86, 0.12); color:#e88b56; border-color:rgba(232, 139, 86, 0.25);">Life Story</span>
                <h3 class="course-name">어려운 보험 용어 타파!</h3>
                <p class="course-sub">카페에서 친한 언니랑 수다 떨듯 쉽게 배우는 경제, 그리고 달러맘의 똑부러진 일상. 지금 들어볼까요?</p>
                <button class="course-btn">스토리 읽기</button>
            </div>
            
            <div class="course-card featured" id="webinar" style="border-color:var(--accent-blue);">
                <span class="course-badge badge-partner" style="background:#2e8b5722; color:#2e8b57; border-color:#2e8b5755;">Webinar / Event</span>
                <h3 class="course-name">2026 달러 전략 라이브</h3>
                <p class="course-sub">달러 전문가와 함께하는 Q&A 및 내 상황에 맞는 맞춤형 컨설팅 맛보기 웨비나.</p>
                <div class="course-schedule-info">
                    📅 매주 화요일 오후 8시<br>온라인 (Zoom 링크 개별 발송)
                </div>
                <button class="course-btn" style="background:var(--accent-blue); color:white; border:none;">신청하기</button>
            </div>
        </div>
    </section>

    <!-- ═══════ CTA SECTION ═══════ -->
    <section class="cta-section">
        <h2 class="cta-title">지금 당신에게 필요한<br><span class="gold">최적의 달러 전략</span>은 무엇일까요?</h2>
        <p class="cta-desc">친한 언니처럼 편안하게, 하지만 전문가의 시선으로 짚어드려요.<br>어려운 용어 없이 내 상황에 딱 맞는 1:1 상담을 받아보세요.</p>
        <button class="btn-gold" style="padding-left:48px; padding-right:48px; font-size:1.1rem; background: linear-gradient(135deg, var(--gold), #2e8b57);" onclick="showApplicationForm()">무료 15분 상담 예약하기</button>
    </section>
"""
# We replace from <!-- ═══════ COURSES SECTION ═══════ --> until <!-- ═══════ CTA SECTION ═══════ --> and its end
content = re.sub(r'<!-- ═══════ COURSES SECTION ═══════ -->.*?</section>', sections_replacement, content, flags=re.DOTALL)


# Footer Replace
footer_replacement = """    <!-- ═══════ FOOTER ═══════ -->
    <footer class="site-footer">
        <div class="footer-inner">
            <div class="footer-top">
                <div class="footer-brand" style="flex:1.5;">
                    <a href="#" class="logo" style="margin-bottom:20px; text-decoration:none;">
                        <div class="logo-icon" style="border-radius:50%; font-size:24px; font-weight:bold; background:linear-gradient(135deg, #c9a84c, #e4c76b); padding-right:2px; padding-bottom:1px; transform:none; display:inline-flex; width:42px; height:42px; align-items:center; justify-content:center; color:#0a0a0f;">D<span style="font-size:12px; margin-left:1px; display:inline-block; transform:translateY(-5px);">♥</span></div>
                        <div class="logo-text" style="color:#f0ece2;">DOLLAR<span style="font-family: 'Noto Sans KR', sans-serif; font-size:1.4rem; padding-left:2px; color:#c9a84c;">MOM</span></div>
                    </a>
                    <p style="font-size:0.9rem; line-height:1.6; color:var(--text-secondary); max-width:400px;">
                        엄마의 눈으로 지키는 달러 자산 보험 메신저.<br>복잡한 금융 상품을 쉽게 풀어드리고, 당신의 든든한 경제적 안전망을 함께 만들어갑니다.
                    </p>
                </div>
                <div style="flex:1;">
                    <div class="footer-heading">Menu</div>
                    <div class="footer-info">
                        <a href="#briefing">달러 브리핑</a><br>
                        <a href="#product101">달러 상품 101</a><br>
                        <a href="#casestudy">케이스 스터디</a><br>
                        <a href="#life">달러맘 라이프</a><br>
                        <a href="#webinar">웨비나/이벤트</a>
                    </div>
                </div>
                <div style="flex:1;">
                    <div class="footer-heading">Contact & Policies</div>
                    <div class="footer-info">
                        <strong>상담문의:</strong> 010-0000-0000<br>
                        <strong>이메일:</strong> support@dollarmom.com<br>
                        <strong>카카오채널:</strong> @dollarmom<br>
                        <a href="#">이용약관</a> | <a href="#">개인정보처리방침</a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom" style="border-top: 1px solid var(--border); margin-top: 10px; padding-top: 20px;">
                <div class="footer-copyright">
                    &copy; 2026 DollarMom. All rights reserved.<br>
                    <small style="color:#e88b56; display:inline-block; margin-top:8px;">* 본 사이트의 내용은 법적/세무적 자문이 아닌 일반 정보 제공 목적이며, 구체적인 금융 상품 가입을 직접 권유하거나 판매하지 않습니다. 가입 시 공식 금융기관 상담을 권장합니다.</small>
                </div>
                <div class="footer-links" style="margin-top:10px;">
                    <a href="https://instagram.com" target="_blank">Instagram</a>
                    <a href="https://blog.naver.com" target="_blank">Naver Blog</a>
                </div>
                
                <div id="footerAdminBtns" class="footer-admin-btns" style="margin-top:20px;">
                    <button class="footer-admin-btn" onclick="showAdminPage()">📋 신청 내역</button>
                    <button class="footer-admin-btn" onclick="loginChatbotAdmin()">⚙️ 챗봇 설정</button>
                    <button class="footer-admin-btn" onclick="toggleHeaderLogin()">🚪 로그아웃</button>
                </div>
            </div>
        </div>
        
    </footer>"""
# Find boundaries of the footer
content = re.sub(r'<!-- ═══════ FOOTER ═══════ -->.*?</footer>', footer_replacement, content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
