# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace variables and dummy data
var_replacement = """        let applicationData = [];
        let allCustomers = [];
        let isLoggedIn = false;
        let adminMenuLoggedIn = false;
        let chatbotOpen = false;
        let chatbotPosition = 'right';
        let apiSettings = {
            chatgpt: { apiKey: '', model: '', enabled: false },
            gemini: { apiKey: '', model: '', enabled: false },
            claude: { apiKey: '', model: '', enabled: false },
            activeProvider: ''
        };
        try {
            var saved = localStorage.getItem('chatbotApiSettings');
            if (saved) {
                var parsed = JSON.parse(saved);
                if (parsed.chatgpt) apiSettings.chatgpt = parsed.chatgpt;
                if (parsed.gemini) apiSettings.gemini = parsed.gemini;
                if (parsed.claude) apiSettings.claude = parsed.claude;
            }
        } catch (e) {}

        // Demo data
        applicationData.push({
            timestamp: '2026-06-10 14:30:25', name: '김자영', phone: '010-1234-5678',
            email: 'kim@example.com', channel: 'web', interest_category: '자녀 교육/유학'
        });
        applicationData.push({
            timestamp: '2026-06-10 15:45:12', name: '이영희', phone: '010-9876-5432',
            email: 'lee@example.com', channel: 'web', interest_category: '달러 예금/적금'
        });"""
content = re.sub(r'        let applicationData = \[\];.*?        \}\);', var_replacement, content, flags=re.DOTALL)


# Replace submitApplication and updateAdminTable
submit_replacement = """        async function submitApplication(e) {
            e.preventDefault();
            
            const consent = document.getElementById('formConsent').checked;
            if (!consent) {
                alert('개인정보 수집 및 이용에 동의해주세요.');
                return;
            }
            
            const data = {
                timestamp: new Date().toLocaleString('ko-KR'),
                name: document.getElementById('formName').value,
                phone: document.getElementById('formPhone').value,
                email: document.getElementById('formEmail').value,
                channel: 'web',
                interest_category: document.getElementById('formInterest').value || '기타'
            };

            // Supabase에 저장
            if (supabaseClient) {
                try {
                    const { error } = await supabaseClient.from('leads').insert([{
                        name: data.name,
                        phone: data.phone,
                        email: data.email,
                        channel: data.channel,
                        interest_category: data.interest_category,
                        created_at: new Date().toISOString()
                    }]);
                    if (error) console.warn('Supabase 저장 실패:', error);
                } catch (err) { console.warn('Supabase 저장 오류:', err); }
            }

            applicationData.push(data);
            alert(`✅ ${data.name}님, 상담 신청이 정상적으로 접수되었습니다!\n\n빠른 시일 내에 연락드리겠습니다. 🙏`);
            e.target.reset();
            closeForm();
        }

        function updateAdminTable() {
            const tbody = document.getElementById('data-table-body');
            tbody.innerHTML = '';
            applicationData.forEach(d => {
                tbody.innerHTML += `<tr><td>${d.timestamp}</td><td>${d.name}</td><td>${d.phone}</td><td>${d.email}</td><td>${d.channel}</td><td>${d.interest_category}</td></tr>`;
            });
            document.getElementById('total-count').textContent = applicationData.length;
        }"""
content = re.sub(r'        async function submitApplication\(e\) \{.*?        \}', submit_replacement, content, flags=re.DOTALL)


# Replace loadCustomersFromSupabase, filterCustomers, downloadExcel
table_funcs_replacement = """        // ═══════ SUPABASE: 고객 데이터 로드 ═══════
        async function loadCustomersFromSupabase() {
            if (!supabaseClient) {
                updateAdminTable();
                return;
            }
            try {
                const { data, error } = await supabaseClient
                    .from('leads')
                    .select('*')
                    .order('created_at', { ascending: false });

                if (error) throw error;

                allCustomers = data || [];
                applicationData = allCustomers.map(c => ({
                    timestamp: c.created_at ? new Date(c.created_at).toLocaleString('ko-KR') : '-',
                    name: c.name || '-',
                    phone: c.phone || '-',
                    email: c.email || '-',
                    channel: c.channel || '-',
                    interest_category: c.interest_category || '-'
                }));
                updateAdminTable();
                var lastEl = document.getElementById('lastUpdated');
                if (lastEl) lastEl.textContent = '마지막 업데이트: ' + new Date().toLocaleString('ko-KR');
            } catch (err) {
                console.warn('고객 데이터 로드 실패:', err);
                updateAdminTable();
            }
        }

        // ═══════ 고객 검색 필터 ═══════
        function filterCustomers() {
            var query = (document.getElementById('customerSearch').value || '').toLowerCase();
            if (!query) {
                updateAdminTable();
                return;
            }
            var filtered = applicationData.filter(function(d) {
                return (d.name || '').toLowerCase().includes(query) ||
                       (d.email || '').toLowerCase().includes(query) ||
                       (d.phone || '').includes(query);
            });
            var tbody = document.getElementById('data-table-body');
            tbody.innerHTML = '';
            filtered.forEach(function(d) {
                tbody.innerHTML += '<tr><td>' + d.timestamp + '</td><td>' + d.name + '</td><td>' + d.phone + '</td><td>' + d.email + '</td><td>' + d.channel + '</td><td>' + d.interest_category + '</td></tr>';
            });
            document.getElementById('total-count').textContent = filtered.length;
            var filterInfo = document.getElementById('customerFilterCount');
            if (filterInfo) filterInfo.textContent = '검색결과: ' + filtered.length + '건 / 전체 ' + applicationData.length + '건';
        }

        // ═══════ 엑셀 다운로드 (SheetJS) ═══════
        function downloadExcel() {
            if (applicationData.length === 0) {
                alert('다운로드할 데이터가 없습니다.');
                return;
            }
            var excelData = applicationData.map(function(d, i) {
                return {
                    'No.': i + 1,
                    '신청일시': d.timestamp,
                    '성명': d.name,
                    '연락처': d.phone,
                    '이메일': d.email,
                    '유입채널': d.channel,
                    '관심분야': d.interest_category
                };
            });
            var wb = XLSX.utils.book_new();
            var ws = XLSX.utils.json_to_sheet(excelData);
            ws['!cols'] = [
                { wch: 5 }, { wch: 20 }, { wch: 12 }, { wch: 16 },
                { wch: 15 }, { wch: 25 }
            ];
            XLSX.utils.book_append_sheet(wb, ws, '상담신청목록');
            var today = new Date().toISOString().slice(0, 10);
            XLSX.writeFile(wb, '상담신청목록_' + today + '.xlsx');
        }"""
content = re.sub(r'        // ═══════ SUPABASE: 고객 데이터 로드 ═══════.*?        // ═══════ 챗봇 위치 선택 ═══════', table_funcs_replacement + '\n\n        // ═══════ 챗봇 위치 선택 ═══════', content, flags=re.DOTALL)


# Also fix admin table headers HTML
admin_table_html = """            <table class="admin-table">
                <thead>
                    <tr>
                        <th>신청일시</th>
                        <th>성명</th>
                        <th>연락처</th>
                        <th>이메일</th>
                        <th>참가경로(채널)</th>
                        <th>관심 분야</th>
                    </tr>
                </thead>"""
content = re.sub(r'            <table class="admin-table">.*?                </thead>', admin_table_html, content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
