/**
 * Gestionnaire de versioning automatique pour EPSIC Students
 * Système de versioning incrémental comme Garibobo Agenda PWA
 */

class VersionManager {
    constructor() {
        this.changelogPath = './changelog.json';
        this.versionPattern = /^(\d+)\.(\d+)\.(\d+)(?:\.(\d+))?$/;
    }

    /**
     * Génère automatiquement la prochaine version
     */
    generateNextVersion(currentVersion) {
        const match = currentVersion.match(this.versionPattern);
        if (!match) {
            console.error('Format de version invalide:', currentVersion);
            return currentVersion;
        }

        const [, major, minor, patch, build] = match;
        
        if (build) {
            // Format: 1.25.1.2 -> 1.25.1.3
            const nextBuild = parseInt(build) + 1;
            return `${major}.${minor}.${patch}.${nextBuild}`;
        } else {
            // Format: 1.25.1 -> 1.25.1.2
            return `${major}.${minor}.${patch}.2`;
        }
    }

    /**
     * Crée une nouvelle entrée de changelog
     */
    createChangelogEntry(version, changes, type = 'fix') {
        const titles = {
            'major': 'Mise à jour majeure',
            'feature': 'Nouvelles fonctionnalités', 
            'fix': 'Corrections et améliorations',
            'security': 'Corrections de sécurité'
        };

        return {
            version: version,
            date: new Date().toISOString().split('T')[0],
            title: titles[type] || 'Mise à jour',
            changes: Array.isArray(changes) ? changes : [changes],
            type: type
        };
    }

    /**
     * Met à jour le changelog avec une nouvelle version
     */
    async updateChangelog(changes, type = 'fix') {
        try {
            // Lire le changelog actuel
            const response = await fetch(this.changelogPath);
            const changelog = await response.json();
            
            // Générer la nouvelle version
            const nextVersion = this.generateNextVersion(changelog.currentVersion);
            
            // Créer la nouvelle entrée
            const newEntry = this.createChangelogEntry(nextVersion, changes, type);
            
            // Ajouter au début du tableau
            changelog.updates.unshift(newEntry);
            changelog.currentVersion = nextVersion;
            
            console.log(`✅ Nouvelle version générée: ${nextVersion}`);
            console.log('📝 Changements:', changes);
            
            return {
                success: true,
                version: nextVersion,
                changelog: changelog
            };
            
        } catch (error) {
            console.error('❌ Erreur lors de la mise à jour du changelog:', error);
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Met à jour le numéro de version dans index.html
     */
    updateVersionInHTML(newVersion) {
        // Cette fonction nécessiterait l'accès au DOM ou au fichier
        // Pour l'instant, on log juste l'instruction
        console.log(`🔄 Mettre à jour la version dans index.html: V.${newVersion}`);
        console.log(`   Remplacer: <span class="version-number"...>V.${this.getCurrentDisplayVersion()}</span>`);
        console.log(`   Par: <span class="version-number"...>V.${newVersion}</span>`);
    }

    /**
     * Obtient la version actuellement affichée
     */
    getCurrentDisplayVersion() {
        const versionElement = document.querySelector('.version-number');
        if (versionElement) {
            return versionElement.textContent.replace('V.', '');
        }
        return 'unknown';
    }

    /**
     * Processus complet de mise à jour de version
     */
    async releaseNewVersion(changes, type = 'fix') {
        console.log('🚀 Démarrage du processus de versioning...');
        
        const result = await this.updateChangelog(changes, type);
        
        if (result.success) {
            this.updateVersionInHTML(result.version);
            
            console.log('📋 Instructions pour finaliser:');
            console.log('1. Mettre à jour le fichier changelog.json');
            console.log('2. Mettre à jour la version dans index.html');
            console.log('3. Pusher les changements sur GitHub');
            console.log('4. Le changelog s\'affichera automatiquement aux utilisateurs');
            
            return result;
        } else {
            console.error('❌ Échec du processus de versioning:', result.error);
            return result;
        }
    }
}

// Instance globale
window.versionManager = new VersionManager();

// Fonction utilitaire pour créer rapidement une nouvelle version
window.newVersion = function(changes, type = 'fix') {
    if (typeof changes === 'string') {
        changes = [changes];
    }
    
    return window.versionManager.releaseNewVersion(changes, type);
};

// Exemples d'utilisation:
// newVersion("Correction du bug de chargement des dossiers");
// newVersion(["Ajout du mode sombre", "Amélioration des performances"], "feature");
// newVersion("Correction critique de sécurité", "security");

console.log('📦 VersionManager initialisé - Utilisez newVersion() pour créer une nouvelle version');
