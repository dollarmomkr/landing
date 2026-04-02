const Parser = require('rss-parser');
const parser = new Parser();

module.exports = async (req, res) => {
  try {
    // 구글 뉴스 RSS (검색어: 달러)
    // q=달러 (URL encoding) -> %EB%8B%AC%EB%9F%AC
    const rssUrl = 'https://news.google.com/rss/search?q=%EB%8B%AC%EB%9F%AC&hl=ko&gl=KR&ceid=KR:ko';
    
    let feed = await parser.parseURL(rssUrl);
    
    // 최근 5개 기사만 추출
    const items = feed.items.slice(0, 5).map(item => {
      // 구글 뉴스는 title 뒤에 ' - 매체명' 이 붙는 경우가 많음
      const titleParts = item.title ? item.title.split(' - ') : [];
      let source = 'Google News';
      let title = item.title || '제목 없음';
      
      if (titleParts.length > 1) {
        source = titleParts.pop(); // 마지막 부분이 대체로 매체명
        title = titleParts.join(' - ');
      }

      return {
        title: title,
        link: item.link,
        pubDate: item.pubDate,
        source: source,
        contentSnippet: item.contentSnippet || ''
      };
    });

    res.status(200).json({
      success: true,
      items: items
    });
  } catch (error) {
    console.error('RSS Parsing Error:', error);
    res.status(500).json({
      success: false,
      message: '뉴스를 불러오는 데 실패했습니다.',
      error: error.message
    });
  }
};
