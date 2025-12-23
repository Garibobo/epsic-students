/**
 * Gestionnaire de mises à jour et changelog pour EPSIC Students
 * Vérifie les nouvelles versions et affiche les notifications
 */

class UpdateManager {
    constructor() {
        this.currentVersion = "1.25.1.2";
        this.changelogUrl = "./changelog.json";
        this.lastCheckKey = "epsic_last_update_check";
        this.lastVersionKey = "epsic_last_version_seen";
        this.checkInterval = 24 * 60 * 60 * 1000; // 24 heures
        this.forceShowChangelog = false; // Afficher le changelog occasionnellement
        this.changelogFrequency = 20; // 1 fois sur 20 visites
    }

    /**
     * Initialise le gestionnaire de mises à jour
     */
    async init() {
        await this.checkForUpdates();
        this.setupPeriodicCheck();
    }

    /**
     * Vérifie s'il y a des mises à jour disponibles
     */
    async checkForUpdates() {
        try {
            const response = await fetch(this.changelogUrl);
            const changelog = await response.json();
            
            const lastVersionSeen = localStorage.getItem(this.lastVersionKey);
            const currentVersion = changelog.currentVersion;
            
            // Afficher le changelog si nouvelle version OU occasionnellement (1/20)
            const shouldShowChangelog = !lastVersionSeen || 
                                      this.compareVersions(currentVersion, lastVersionSeen) > 0 ||
                                      this.shouldShowChangelogRandomly();
            
            if (shouldShowChangelog) {
                this.showUpdateNotification(changelog);
                localStorage.setItem(this.lastVersionKey, currentVersion);
            }
            
            localStorage.setItem(this.lastCheckKey, Date.now().toString());
            
        } catch (error) {
            console.log('Impossible de vérifier les mises à jour:', error);
        }
    }

    /**
     * Compare deux versions (format x.y.z)
     */
    compareVersions(version1, version2) {
        const v1Parts = version1.split('.').map(Number);
        const v2Parts = version2.split('.').map(Number);
        
        for (let i = 0; i < Math.max(v1Parts.length, v2Parts.length); i++) {
            const v1Part = v1Parts[i] || 0;
            const v2Part = v2Parts[i] || 0;
            
            if (v1Part > v2Part) return 1;
            if (v1Part < v2Part) return -1;
        }
        return 0;
    }

    /**
     * Affiche la notification de mise à jour
     */
    showUpdateNotification(changelog) {
        const latestUpdate = changelog.updates[0];
        
        // Créer la notification
        const notification = document.createElement('div');
        notification.className = 'update-notification';
        notification.innerHTML = `
            <div class="update-content">
                <div class="update-header">
                    <span class="update-icon">🎉</span>
                    <h3>Nouvelle mise à jour disponible !</h3>
                    <button class="update-close" onclick="this.parentElement.parentElement.parentElement.remove()">×</button>
                </div>
                <div class="update-body">
                    <p><strong>Version ${latestUpdate.version}</strong> - ${latestUpdate.title}</p>
                    <ul class="update-changes">
                        ${latestUpdate.changes.map(change => `<li>${change}</li>`).join('')}
                    </ul>
                </div>
                <div class="update-actions">
                    <button class="btn-changelog" onclick="updateManager.showFullChangelog()">
                        Voir tout l'historique
                    </button>
                    <button class="btn-dismiss" onclick="this.parentElement.parentElement.parentElement.remove()">
                        Compris !
                    </button>
                </div>
            </div>
        `;
        
        document.body.appendChild(notification);
        
        // Animation d'apparition
        setTimeout(() => notification.classList.add('show'), 100);
        
        // Auto-masquage après 10 secondes
        setTimeout(() => {
            if (notification.parentElement) {
                notification.classList.remove('show');
                setTimeout(() => notification.remove(), 300);
            }
        }, 10000);
    }

    /**
     * Affiche le changelog complet dans une modal
     */
    async showFullChangelog() {
        try {
            const response = await fetch(this.changelogUrl);
            const changelog = await response.json();
            
            const modal = document.createElement('div');
            modal.className = 'changelog-modal';
            modal.innerHTML = `
                <div class="changelog-content">
                    <div class="changelog-header">
                        <h2>📋 Historique des mises à jour</h2>
                        <button class="changelog-close" onclick="this.parentElement.parentElement.parentElement.remove()">×</button>
                    </div>
                    <div class="changelog-body">
                        ${changelog.updates.map(update => `
                            <div class="changelog-item ${update.type}">
                                <div class="changelog-version">
                                    <span class="version-badge ${update.type}">v${update.version}</span>
                                    <span class="version-date">${this.formatDate(update.date)}</span>
                                </div>
                                <h3>${update.title}</h3>
                                <ul>
                                    ${update.changes.map(change => `<li>${change}</li>`).join('')}
                                </ul>
                            </div>
                        `).join('')}
                    </div>
                    <div class="changelog-footer">
                        <p>Version actuelle: <strong>${changelog.currentVersion}</strong></p>
                    </div>
                </div>
            `;
            
            document.body.appendChild(modal);
            setTimeout(() => modal.classList.add('show'), 100);
            
            // Fermeture en cliquant à l'extérieur
            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    modal.classList.remove('show');
                    setTimeout(() => modal.remove(), 300);
                }
            });
            
        } catch (error) {
            console.error('Erreur lors du chargement du changelog:', error);
        }
    }

    /**
     * Formate une date au format français
     */
    formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString('fr-FR', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    }

    /**
     * Configure la vérification périodique
     */
    setupPeriodicCheck() {
        const lastCheck = localStorage.getItem(this.lastCheckKey);
        const now = Date.now();
        
        if (!lastCheck || (now - parseInt(lastCheck)) > this.checkInterval) {
            this.checkForUpdates();
        }
        
        // Vérification toutes les heures quand la page est active
        setInterval(() => {
            if (document.visibilityState === 'visible') {
                this.checkForUpdates();
            }
        }, 60 * 60 * 1000);
    }

    /**
     * Détermine si le changelog doit être affiché aléatoirement (1 fois sur 20)
     */
    shouldShowChangelogRandomly() {
        const randomChance = Math.floor(Math.random() * this.changelogFrequency) + 1;
        return randomChance === 1; // 1 chance sur 20
    }

    /**
     * Force une vérification manuelle
     */
    async forceCheck() {
        localStorage.removeItem(this.lastVersionKey);
        await this.checkForUpdates();
    }

    /**
     * Génère automatiquement la prochaine version (comme Garibobo Agenda)
     */
    generateNextVersion(currentVersion) {
        const parts = currentVersion.split('.');
        if (parts.length === 4) {
            // Format: 1.25.1.2 -> 1.25.1.3
            const lastPart = parseInt(parts[3]) + 1;
            return `${parts[0]}.${parts[1]}.${parts[2]}.${lastPart}`;
        } else if (parts.length === 3) {
            // Format: 1.25.1 -> 1.25.1.2
            return `${currentVersion}.2`;
        }
        return currentVersion;
    }

    /**
     * Met à jour automatiquement la version dans le changelog
     */
    async updateVersioning(newChanges, changeType = 'fix') {
        try {
            const response = await fetch(this.changelogUrl);
            const changelog = await response.json();
            
            const nextVersion = this.generateNextVersion(changelog.currentVersion);
            const today = new Date().toISOString().split('T')[0];
            
            const newUpdate = {
                version: nextVersion,
                date: today,
                title: this.getUpdateTitle(changeType),
                changes: newChanges,
                type: changeType
            };
            
            // Ajouter la nouvelle version au début
            changelog.updates.unshift(newUpdate);
            changelog.currentVersion = nextVersion;
            
            console.log('Nouvelle version générée:', nextVersion);
            return changelog;
            
        } catch (error) {
            console.error('Erreur lors de la mise à jour du versioning:', error);
            return null;
        }
    }

    /**
     * Génère un titre automatique selon le type de mise à jour
     */
    getUpdateTitle(changeType) {
        const titles = {
            'major': 'Mise à jour majeure',
            'feature': 'Nouvelles fonctionnalités',
            'fix': 'Corrections et améliorations',
            'security': 'Corrections de sécurité'
        };
        return titles[changeType] || 'Mise à jour';
    }
}

// Instance globale
const updateManager = new UpdateManager();

// Initialisation automatique avec affichage forcé du changelog
document.addEventListener('DOMContentLoaded', () => {
    console.log('UpdateManager: Initialisation avec changelog forcé');
    updateManager.init();
});

// Fonction globale pour ajouter facilement de nouvelles versions
window.addNewVersion = function(changes, type = 'fix') {
    updateManager.updateVersioning(changes, type).then(changelog => {
        if (changelog) {
            console.log('Nouvelle version ajoutée:', changelog.currentVersion);
            // Ici vous pourriez sauvegarder le changelog mis à jour
        }
    });
};

// Exemple d'utilisation pour les prochaines mises à jour:
// addNewVersion([
//     "Correction du bug X",
//     "Amélioration de la performance Y"
// ], 'fix');
