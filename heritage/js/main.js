        const stageData = {
            csv: {
                icon: '🌊',
                name: 'CSV/Background',
                subtitle: 'Commons / Simulation',
                neuro: '.csv',
                web: 'Background / Commons',
                role: 'Raw Experience, Simulation',
                description: 'This is raw experience, tabulated. No credential yet. No judgment. Just pre-epistemic data. The world as it is.'
            },
            py: {
                icon: '❤️',
                name: 'Python/Methods',
                subtitle: 'Boundaries / Rules',
                neuro: '.py',
                web: 'Methods / Boundaries',
                role: 'Define Rules & Constraints',
                description: 'Now we define rules, test logic, establish how to operate. Credentialing lurks here as initial constraints. Here’s how to play the game, if you want to be seen.'
            },
            jinja: {
                icon: '🌀',
                name: 'Jinja/Scenarios',
                subtitle: 'Ukusoma / Games',
                neuro: '.jinja',
                web: 'Scenarios / Ukusoma',
                role: 'Simulation & Play',
                description: 'Simulation becomes play. Ukusoma (“the taste of self”) is the erotic loop — credentials allow or forbid your entry. Try out a version of you — but only within approved bounds.'
            },
            html: {
                icon: '🐬',
                name: 'HTML/Results',
                subtitle: 'Credential / Equilibria',
                neuro: '.html',
                web: 'Results / Credential',
                role: 'Accredited Output & Legibility',
                description: 'Credential emerges here as a rendered output — stable, polished, shareable. Credential = “This version of you is valid.” You can show this to the world. We vouch for it. Accreditation is what gives .html teeth. Without it, it’s just “some website.” With it, it’s “official.”'
            },
            yaml: {
                icon: '🔁',
                name: 'YAML/Conclusion',
                subtitle: 'Monopoly / Illusion',
                neuro: '.yaml',
                web: 'Conclusion / Monopoly',
                role: 'Truth Monopoly & Feedback Loop',
                description: 'Now the feedback loop. YAML is meta-structure. Credential becomes an illusion of exclusivity, a kind of truth monopoly. All roads lead to us — or so we’ve convinced you. Accreditation is recursive: “We trust them because they were accredited by people we already trust.” That’s not proof — that’s a trust echo chamber.'
            }
        };
        
        function createStars() {
            const cosmicBg = document.getElementById('cosmicBg');
            for (let i = 0; i < 100; i++) {
                const star = document.createElement('div');
                star.className = 'star';
                star.style.left = Math.random() * 100 + '%';
                star.style.top = Math.random() * 100 + '%';
                star.style.width = Math.random() * 3 + 1 + 'px';
                star.style.height = star.style.width;
                star.style.animationDelay = Math.random() * 3 + 's';
                cosmicBg.appendChild(star);
            }
        }
        
        document.querySelectorAll('.stage').forEach(stage => {
            stage.addEventListener('click', () => {
                const stageType = stage.dataset.stage;
                openDetail(stageType);
            });
            
            stage.addEventListener('mouseenter', () => {
                stage.classList.add('active');
            });
            
            stage.addEventListener('mouseleave', () => {
                stage.classList.remove('active');
            });
        });
        
        function openDetail(stageType) {
            const data = stageData[stageType];
            document.getElementById('detailIcon').textContent = data.icon;
            document.getElementById('detailName').textContent = data.name;
            document.getElementById('detailNeuro').innerHTML = data.neuro;
            document.getElementById('detailWeb').innerHTML = data.web;
            document.getElementById('detailRole').innerHTML = data.role;
            document.getElementById('detailDescription').innerHTML = data.description;
            document.getElementById('detailPanel').classList.add('active');
        }
        
        function closeDetail() {
            document.getElementById('detailPanel').classList.remove('active');
        }
        
        function setView(view) {
            document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            const container = document.querySelector('.spiral-container');
            container.style.transform = view === 'cycle' ? 'rotate(360deg)' : 'rotate(0deg)';
            container.style.transition = 'transform 2s ease-in-out';
        }
        
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') closeDetail();
        });
        
        createStars();
        
        setInterval(() => {
            const stages = document.querySelectorAll('.stage');
            stages.forEach((stage, index) => {
                setTimeout(() => {
                    stage.style.transform += ' rotate(360deg)';
                    setTimeout(() => {
                        stage.style.transform = stage.style.transform.replace(' rotate(360deg)', '');
                    }, 1000);
                }, index * 200);
            });
        }, 15000);
